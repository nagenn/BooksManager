
from models import add_book, get_all_books

def test_add_book():
    add_book("Test","Author")
    books = get_all_books()
    assert len(books) > 0
