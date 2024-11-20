import json
import os
import pytest
from library import Book, Library

@pytest.fixture
def library():
    """Создает временную библиотеку для тестирования."""
    lib = Library(filename='test_library.json')
    lib.books = []  # Очищаем книги для тестирования
    yield lib
    if os.path.exists('test_library.json'):
        os.remove('test_library.json')  # Удаляем файл после тестов

def test_add_book(library):
    """Тест на добавление книги."""
    library.add_book("1984", "George Orwell", 1949)
    assert len(library.books) == 1
    assert library.books[0].title == "1984"
    assert library.books[0].author == "George Orwell"
    assert library.books[0].year == 1949
    assert library.books[0].status == "в наличии"

def test_remove_book(library):
    """Тест на удаление книги."""
    library.add_book("Brave New World", "Aldous Huxley", 1932)
    library.remove_book(1)
    assert len(library.books) == 0

def test_remove_nonexistent_book(library):
    """Тест на попытку удалить несуществующую книгу."""
    library.add_book("Fahrenheit 451", "Ray Bradbury", 1953)
    library.remove_book(999)  # некорректный ID
    assert len(library.books) == 1  # книга должна остаться

def test_search_book(library):
    """Тест на поиск книги по названию."""
    library.add_book("The Catcher in the Rye", "J.D. Salinger", 1951)
    results = library.search_books("Catcher")
    assert len(results) == 1
    assert results[0].title == "The Catcher in the Rye"

def test_change_status(library):
    """Тест на изменение статуса книги."""
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    library.change_status(1, "выдана")
    assert library.books[0].status == "выдана"

def test_change_status_nonexistent_book(library):
    """Тест на попытку изменить статус несуществующей книги."""
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.change_status(999, "выдана")  # некорректный ID
    assert library.books[0].status == "в наличии"  # статус должен остаться прежним

def test_load_books(library):
    """Тест на загрузку книг из файла JSON."""
    library.add_book("Moby Dick", "Herman Melville", 1851)
    library.save_books()

    # Создаем новый объект библиотеки и загружаем книги
    new_library = Library(filename='test_library.json')
    assert len(new_library.books) == 1
    assert new_library.books[0].title == "Moby Dick"

if __name__ == "__main__":
    pytest.main()
