from flask import render_template, request, redirect, url_for, flash, session
from app.models import Book , User
from app import db
from app.books import books_routes
from app.decorators import login_required

@books_routes.route('/add-book', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        image = request.files['image'].read() if 'image' in request.files else None
        new_book = Book(title=title, author=author, image=image, user_id=session['user_id'])
        
        db.session.add(new_book)
        db.session.commit()
        
        flash("Book added successfully!")
        return redirect(url_for('home.profile'))

    return render_template('add_book.html')

@books_routes.route('/view-books')
@login_required
def view_books():
    books = Book.query.all()
    return render_template('view_books.html', books=books)

@books_routes.route('/delete-book/<int:book_id>')
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book and book.owner.id == session['user_id']:
        db.session.delete(book)
        db.session.commit()
        flash("Book deleted successfully!")
    else:
        flash("You do not have permission to delete this book!")
    return redirect(url_for('home.profile'))


@books_routes.route('/add-to-user/<int:book_id>', methods=['POST'])
def add_to_user(book_id):
    if 'user_id' not in session:
        flash("You must be logged in to add books to your profile.")
        return redirect(url_for('auth.login'))

    book = Book.query.get(book_id)
    if not book:
        flash("Book not found.")
        return redirect(url_for('books.view_books'))

    user = User.query.get(session['user_id'])

    # Use user_id instead of owner_id
    if book.user_id != user.id:  # Checking if the book belongs to someone else
        user.books.append(book)  # Assuming this relationship exists in your model
        db.session.commit()
        flash(f'Book "{book.title}" added to your collection.')
    else:
        flash("You cannot add your own book.")

    return redirect(url_for('books.view_books'))