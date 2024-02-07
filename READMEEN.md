# Task Manager with Flask and MySQL

The Task Manager is a web application developed with Flask and MySQL that allows users to register pending tasks and mark them as completed.

## Installation

To run the application locally, follow these steps:

1. Clone this repository on your local machine:

    ```bash
    git clone https://github.com/tiantaii/Gesty
    ```

2. Navigate to the project directory:

    ```bash
    cd Gesty
    ```

3. Create a virtual environment and install the dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/Linux based systems
    # Or
    venv\Scripts\activate  # For Windows based systems
    pip install -r requirements.txt
    ```

4. Configure the environment variables:

    - `FLASK_DATABASE_HOST`: The MySQL database host address.
    - `FLASK_DATABASE_USER`: The MySQL database username.
    - `FLASK_DATABASE_PASSWORD`: The MySQL database password.
    - `FLASK_DATABASE`: The MySQL database name.

5. Initialize the database:

    ```bash
    flask init-db
    ```

6. Run the application:

    ```bash
    flask run
    ```

7. Open your web browser and visit `http://localhost:5000` to access the task manager.

## Features

- **User Registration**: Users can register to create an account in the application.
- **Login**: Users can log in with their username and password.
- **Add Tasks**: Users can add new tasks by specifying a description.
- **Mark Tasks as Completed**: Users can mark tasks as completed.
- **Delete Tasks**: Users can delete tasks they no longer need.

## Usage

1. **Registration and Login**: To get started, a user needs to register in the application or log in if they already have an account.

2. **Add Tasks**: Once logged in, users can add new tasks by clicking the "Add Task" button and providing a task description.

3. **Manage Tasks**: Users can mark tasks as completed by clicking the checkbox next to each task. They can also delete tasks by clicking the delete button.

4. **Logout**: When finished using the application, make sure to log out to protect your account.

## Contributions

Contributions are welcome. If you find any issues or have any improvements you suggest, feel free to open an issue or submit a pull request on the [project repository](https://github.com/tiantaii/Gesty).

## Credits

This application was developed by Santiago Marr as part of a web development learning project with Flask and MySQL.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
