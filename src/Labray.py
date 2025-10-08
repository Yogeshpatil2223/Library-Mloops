

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"⚠️ Book ID {book_id} already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(f"✅ Book '{title}' added successfully.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"❌ Book '{removed.title}' removed.")
        else:
            print(f"⚠️ Book ID {book_id} not found.")

    def issue_book(self, book_id):
        if book_id in self.books and self.books[book_id].available:
            self.books[book_id].available = False
            print(f"📕 '{self.books[book_id].title}' has been issued.")
        else:
            print("⚠️ Book not available or doesn't exist.")

    def return_book(self, book_id):
        if book_id in self.books and not self.books[book_id].available:
            self.books[book_id].available = True
            print(f"📗 '{self.books[book_id].title}' has been returned.")
        else:
            print("⚠️ Book not found or already available.")

    def show_books(self):
        if not self.books:
            print("📚 No books in the library.")
            return
        for book in self.books.values():
            print(book)


# Example usage
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
