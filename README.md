# Book Management System

This is a simple Flask-based web application that allows users to register, log in, and manage their personal book collections. Admin users have additional functionality to manage all user accounts and books within the system.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Admin Dashboard**: Admins can view and manage all users and their books.
- **Book Management**: Users can add, view, and remove books from their personal collection. Admins can edit or delete any book.
- **Image Upload**: Users can upload images of their books.
- **Password Security**: Passwords are hashed and stored securely.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Werkzeug for password hashing

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ibrahimsaber1/book-management.git
   cd book-management
   ```
2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Set up the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:

    ```bash
    flask run
    ```

The app should now be running at http://127.0.0.1:5000.

## Usage

### User Registration & Login

Users can register and log in to manage their personal library of books. They can add new books to their collection, view them, and remove them if needed.

### Admin Functionality

Admins have extra privileges:

- They can view and edit all users and books.
- They can delete users or books.

## Project Structure

```bash
.
├── app/
│   ├── __init__.py          # Initializes the Flask app and registers blueprints
│   ├── models.py            # Database models for User and Book
│   ├── templates/           # HTML templates for the application
│   ├── static/              # Static files such as CSS and images
│   └── routes/              # Defines routes for users and admin
├── migrations/              # Database migration scripts
├── venv/                    # Virtual environment
├── main.py                  # Entry point for the Flask app
├── config.py                # Configuration for the app (development, production, etc.)
└── README.md                # This file
```


## Models

### User Model
- Contains fields for `id`, `username`, `password`, and `is_admin`.
- Establishes a relationship with the `Book` model via the `books` field.

### Book Model
- Contains fields for `id`, `title`, `author`, `image`, and `user_id`.
- Each book is linked to a `User` via `user_id`.

## Routes

### User Routes
- `/signup`: User registration.
- `/login`: User login.
- `/profile`: View user profile and books.
- `/add-book`: Add a book to the user's collection.
- `/delete-book/<int:book_id>`: Delete a book from the user's collection.

### Admin Routes
- `/admin-dashboard`: View all users and books.
- `/admin/edit-user/<int:user_id>`: Edit user details.
- `/admin/delete-user/<int:user_id>`: Delete a user.
- `/admin/edit-book/<int:book_id>`: Edit a book's details.
- `/admin/delete-book/<int:book_id>`: Delete a book.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
