from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from gesty.auth import login_required
from gesty.db import get_db

bp = Blueprint('gesty', __name__)

@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        'SELECT t.id, t.description, u.username, t.completed, t.created_at '
        'FROM gesty t JOIN user u ON t.created_by = u.id ORDER BY created_at DESC'
    )
    todos = c.fetchall()
    return render_template('gesty/index.html', todos=todos)

@bp.route('/create', methods=('GET', 'POST')) 
@login_required
def create():
    if request.method == 'POST':
        description = request.form['description']
        error = None
        if not description:
            error = 'Por favor ingresa una descripción'
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                'INSERT INTO gesty (description, completed, created_by) VALUES (%s, %s, %s)',
                (description, False, g.user['id'])
            )
            db.commit()
            return redirect(url_for('gesty.index'))
    return render_template('gesty/create.html')

def get_todo(id):
    db, c = get_db()
    c.execute(
        'SELECT t.id, t.description, t.completed, t.created_at, t.created_by, u.username '
        'FROM gesty t JOIN user u ON t.created_by = u.id WHERE t.id = %s',
        (id,)
    )
    todo = c.fetchone()
    if todo is None:
        abort(404, f'Gesty id {id} not found')
    return todo

@bp.route('/<int:id>/update', methods=('GET', 'POST'))  
@login_required
def update(id):
    todo = get_todo(id)
    if request.method == 'POST':
        description = request.form['description']
        completed = True if request.form.get('completed') == 'on' else False
        db, c = get_db()
        c.execute(
            'UPDATE gesty SET description = %s, completed = %s WHERE id = %s',
            (description, completed, id)
        )
        db.commit()
        return redirect(url_for('gesty.index'))
    return render_template('gesty/update.html', todo=todo)

@bp.route('/<int:id>/delete', methods=('POST',))  
@login_required
def delete(id):
    db, c = get_db()
    c.execute('DELETE FROM gesty WHERE id = %s AND created_by = %s', (id, g.user['id']))
    db.commit()
    return redirect(url_for('gesty.index'))

