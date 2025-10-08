import sys, os
# Add parent directory to path so src can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Labray import Library


def test_add_book():
    lib = Library()
    result = lib.add_book(1, "Python Basics", "John Doe")
    assert result is True
    assert 1 in lib.books
    assert lib.books[1].title == "Python Basics"
    assert lib.books[1].available is True


def test_issue_and_return_book():
    lib = Library()
    lib.add_book(2, "ML Guide", "Jane Smith")

    issue_result = lib.issue_book(2)
    assert issue_result is True
    assert lib.books[2].available is False

    return_result = lib.return_book(2)
    assert return_result is True
    assert lib.books[2].available is True


def test_remove_book():
    lib = Library()
    lib.add_book(3, "AI Revolution", "Alan Turing")
    remove_result = lib.remove_book(3)
    assert remove_result is True
    assert 3 not in lib.books
