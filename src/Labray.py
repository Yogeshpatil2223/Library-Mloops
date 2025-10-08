class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id}: {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        """Add a new book to the library"""
        if book_id in self.books:
            print(f"⚠️ Book ID {book_id} already exists.")
            return False
        self.books[book_id] = Book(book_id, title, author)
        print(f"✅ Book '{title}' added successfully.")
        return True

    def remove_book(self, book_id):
        """Remove a book by ID"""
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"❌ Book '{removed.title}' removed.")
            return True
        else:
            print(f"⚠️ Book ID {book_id} not found.")
            return False

    def issue_book(self, book_id):
        """Issue a book to a reader"""
        if book_id in self.books and self.books[book_id].available:
            self.books[book_id].available = False
            print(f"📕 '{self.books[book_id].title}' has been issued.")
            return True
        else:
            print("⚠️ Book not available or doesn't exist.")
            return False

    def return_book(self, book_id):
        """Return a previously issued book"""
        if book_id in self.books and not self.books[book_id].available:
            self.books[book_id].available = True
            print(f"📗 '{self.books[book_id].title}' has been returned.")
            return True
        else:
            print("⚠️ Book not found or already available.")
            return False

    def show_books(self):
        """Display all books"""
        if not self.books:
            print("📚 No books in the library.")
            return
        for book in self.books.values():
            print(book)


if __name__ == "__main__":
    lib = Library()
    lib.add_book(1, "Python Basics", "John Doe")
    lib.add_book(2, "Data Science Handbook", "Jane Smith")
    lib.show_books()

    lib.issue_book(1)
    lib.show_books()

    lib.return_book(1)
    lib.show_books()

    lib.remove_book(2)
    lib.show_books()
