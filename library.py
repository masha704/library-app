import json
import os


class Book:
    def __init__(self, title, author, year):
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def to_dict(self):
        """Возвращает словарь представление книги."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Загружает книги из файла JSON."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = [self.dict_to_book(item) for item in data]

    def dict_to_book(self, data):
        """Создает книгу из словаря."""
        book = Book(data['title'], data['author'], data['year'])
        book.id = data['id']
        book.status = data['status']
        return book

    def save_books(self):
        """Сохраняет книги в файл JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Добавляет новую книгу в библиотеку."""
        new_book = Book(title, author, year)
        new_book.id = len(self.books) + 1  # простая генерация id
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена.")

    def remove_book(self, book_id):
        """Удаляет книгу из библиотеки по id."""
        book = next((b for b in self.books if b.id == book_id), None)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с id {book_id} удалена.")
        else:
            print("Книга не найдена.")

    def search_books(self, keyword):
        """Ищет книги по названию, автору или году."""
        results = [
            b for b in self.books if keyword.lower() in b.title.lower()
            or keyword.lower() in b.author.lower() or keyword == str(b.year)
        ]
        return results

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Нет книг в библиотеке.")
            return
        for book in self.books:
            print(f"id: {book.id}, title: {book.title}, author: {book.author}, "
                  f"year: {book.year}, status: {book.status}")

    def change_status(self, book_id, new_status):
        """Изменяет статус книги на указанный."""
        book = next((b for b in self.books if b.id == book_id), None)
        if book:
            if new_status in ["в наличии", "выдана"]:
                book.status = new_status
                self.save_books()
                print(f"Статус книги с id {book_id} изменен на '{new_status}'.")
            else:
                print("Некорректный статус.")
        else:
            print("Книга не найдена.")


def main():
    """Главная функция для работы с библиотекой."""
    # Выбор языка
    language = input("Выберите язык (ru/en): ").strip().lower()
    if language not in ["ru", "en"]:
        print("Неверный выбор языка. Приложение будет запущено на русском.")

        language = "ru"

    library = Library()
    while True:
        if language == "ru":
            print("\n1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Найти книгу")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выход")
            choice = input("Выберите опцию: ")

            if choice == '1':
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания: ")
                library.add_book(title, author, year)
            elif choice == '2':
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
            elif choice == '3':
                keyword = input("Введите название или автора книги для поиска: ")
                results = library.search_books(keyword)
                for book in results:
                    print(
                        f"Найдено: id: {book.id}, title: {book.title}, author: {book.author}, year: {book.year}, status: {book.status}")
            elif choice == '4':
                library.display_books()
            elif choice == '5':
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status = input("Введите новый статус (в наличии/выдана): ")
                library.change_status(book_id, new_status)
            elif choice == '6':
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")

        else:  # English language options
            print("\n1. Add Book")
            print("2. Remove Book")
            print("3. Search Book")
            print("4. Display All Books")
            print("5. Change Book Status")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter publication year: ")
                library.add_book(title, author, year)
            elif choice == '2':
                book_id = int(input("Enter the ID of the book to remove: "))
                library.remove_book(book_id)
            elif choice == '3':
                keyword = input("Enter book title or author to search: ")
                results = library.search_books(keyword)
                for book in results:
                    print(
                        f"Found: id: {book.id}, title: {book.title}, author: {book.author}, year: {book.year}, status: {book.status}")
            elif choice == '4':
                library.display_books()
            elif choice == '5':
                book_id = int(input("Enter ID of the book to change status: "))
                new_status = input("Enter new status (available/checked out): ")
                library.change_status(book_id, new_status)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
