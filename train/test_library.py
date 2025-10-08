from src.Labray import Library

def test_add_book():
    lib = Library()
    lib.add_book(1, "Python Basics", "John Doe")
    assert 1 in lib.books
    assert lib.books[1].title == "Python Basics"
    assert lib.books[1].available is True

def test_issue_and_return_book():
    lib = Library()
    lib.add_book(2, "ML Guide", "Jane Smith")

    lib.issue_book(2)
    assert lib.books[2].available is False

    lib.return_book(2)
    assert lib.books[2].available is True
