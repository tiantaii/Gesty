# Gestor de Tareas con Flask y MySQL

El Gestor de Tareas es una aplicación web desarrollada con Flask y MySQL que permite a los usuarios registrar tareas pendientes y marcarlas como completadas.

## Instalación

Para ejecutar la aplicación localmente, sigue estos pasos:

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tiantaii/Gesty
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd Gesty
    ```

3. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas basados en Unix/Linux
    # O bien
    venv\Scripts\activate  # Para sistemas basados en Windows
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno:

    - `FLASK_DATABASE_HOST`: La dirección del host de la base de datos MySQL.
    - `FLASK_DATABASE_USER`: El nombre de usuario de la base de datos MySQL.
    - `FLASK_DATABASE_PASSWORD`: La contraseña de la base de datos MySQL.
    - `FLASK_DATABASE`: El nombre de la base de datos MySQL.

5. Inicializa la base de datos:

    ```bash
    flask init-db
    ```

6. Ejecuta la aplicación:

    ```bash
    flask run
    ```

7. Abre tu navegador web y visita `http://localhost:5000` para acceder al gestor de tareas.

## Funcionalidades

- **Registro de Usuarios**: Los usuarios pueden registrarse para crear una cuenta en la aplicación.
- **Inicio de Sesión**: Los usuarios pueden iniciar sesión con su nombre de usuario y contraseña.
- **Agregar Tareas**: Los usuarios pueden agregar nuevas tareas especificando una descripción.
- **Marcar Tareas como Completadas**: Los usuarios pueden marcar las tareas como completadas.
- **Eliminar Tareas**: Los usuarios pueden eliminar las tareas que ya no necesitan.

## Uso

1. **Registro e Inicio de Sesión**: Para comenzar, un usuario necesita registrarse en la aplicación o iniciar sesión si ya tiene una cuenta.

2. **Agregar Tareas**: Una vez que haya iniciado sesión, puede agregar nuevas tareas haciendo clic en el botón "Agregar Tarea" y proporcionando una descripción de la tarea.

3. **Administrar Tareas**: Puede marcar las tareas como completadas haciendo clic en la casilla de verificación junto a cada tarea. También puede eliminar las tareas haciendo clic en el botón de eliminación.

4. **Cerrar Sesión**: Cuando haya terminado de usar la aplicación, asegúrese de cerrar sesión para proteger su cuenta.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora que sugieres, no dudes en abrir un problema o enviar una solicitud de extracción en el [repositorio del proyecto](https://github.com/tiantaii/Gesty).

## Créditos

Esta aplicación fue desarrollada por Santiago Marr como parte de un proyecto de aprendizaje de desarrollo web con Flask y MySQL.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
