# Библиотечное приложение / Library Application

## Описание

Это приложение представляет собой простую библиотеку управления книгами. Пользователи могут добавлять, удалять, изменять статус книг и выполнять поиск по книгам. Данные о книгах сохраняются в файле JSON, что позволяет сохранять состояние библиотеки между запусками приложения.

This application is a simple library management system. Users can add, remove, change the status of books, and search for them. Book data is saved in a JSON file, which allows the state of the library to be preserved between application runs.

## Функционал / Features

### Основные функции:
1. **Добавление книги**: Позволяет добавлять книги с указанием названия, автора и года издания.
2. **Удаление книги**: Удаляет книгу из библиотеки по ее идентификатору (ID).
3. **Поиск книги**: Позволяет искать книги по названию, автору или году издания.
4. **Отображение всех книг**: Выводит список всех книг в библиотеке с их деталями.
5. **Изменение статуса книги**: Изменяет статус книги (например, на "в наличии" или "выдана").
6. **Сохранение и загрузка данных**: Автоматически сохраняет данные о книгах в файл JSON и загружает их при старте приложения.

### Main features:
1. **Add Book**: Allows adding books with a title, author, and publication year.
2. **Remove Book**: Removes a book from the library by its identifier (ID).
3. **Search Book**: Allows searching for books by title, author, or publication year.
4. **Display All Books**: Lists all books in the library with their details.
5. **Change Book Status**: Changes a book's status (e.g., to "available" or "checked out").
6. **Save and Load Data**: Automatically saves book data to a JSON file and loads it on application startup.

## Установка / Installation

1. Убедитесь, что у вас установлен Python 3.x: [Скачать Python](https://www.python.org/downloads/)
2. Клонируйте этот репозиторий или скачайте архив с кодом:
   ```bash
   git clone https://github.com/yourusername/library-app.git
   cd library-app
3. Установите необходимые зависимости (в данный момент приложение не требует дополнительных библиотек, но вы можете использовать pytest для запуска тестов):
      pip install pytest

## Installation
1. Make sure you have Python 3.x installed: [Download Python](https://www.python.org/downloads/)
2. Clone this repository or download the code archive:
      git clone https://github.com/yourusername/library-app.git
   cd library-app
3. Install the required dependencies (currently, the application does not require additional libraries, but you can use pytest to run tests):
      pip install pytest

## Использование / Usage
1. Запустите приложение:
      python library.py
2. Выберите одну из опций из меню:
   - Добавить книгу
   - Удалить книгу
   - Найти книгу
   - Отобразить все книги
   - Изменить статус книги
   - Выход

## Usage
1. Run the application:
      python library.py
2. Select one of the options from the menu:
   - Add Book
   - Remove Book
   - Search Book
   - Display All Books
   - Change Book Status
   - Exit
  
## Тестирование / Testing

Для запуска тестов выполните следующую команду:

pytest test_library.py

To run the tests, use the following command:

pytest test_library.py
