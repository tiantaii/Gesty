import functools
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from gesty.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))  # Eliminar espacio en 'GET '
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()  # Asegurarse de que get_db() retorna correctamente la base de datos y el cursor
        error = None

        # Corregir consulta SQL para incluir placeholder y parámetro username
        db.execute(
            'SELECT id FROM user WHERE username = %s', (username,)
        )
        if not username:
            error = 'Se requiere usuario.'  # Corregir errores de tipografía
        elif not password:
            error = 'Se requiere contraseña.'
        elif db.fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (%s, %s)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET, ''POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form ['password']
        db, c=get_db()
        error=None
        c.execute(
            'select*from user where username = %s', (username,)
        )
        user = c.fetchone()
        if user is None:
            error='Usuario y/o contraseña incorrectos'
        elif not check_password_hash(user['password'], password):
            error='Usuario y/o contraseña incorrectos'
        
        if  error is not None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')
    
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
