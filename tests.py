from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_empty_name_not_added(self):
        name_book = ''
        book = BooksCollector()
        book.add_new_book(name_book)
        assert name_book not in book.books_genre

    @pytest.mark.parametrize('name_book', ['КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига',
                                           'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаК',
                                           'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаКн'])
    def test_add_new_book_name_over_forty_chars_rejected(self, name_book):
        book = BooksCollector()
        book.add_new_book(name_book)
        assert name_book not in book.books_genre

    @pytest.mark.parametrize('name_book', ['Война и мир', 'Я', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    def test_add_new_book_valid_value_one_to_forty_chars_added_successfully(self, name_book):
        book = BooksCollector()
        book.add_new_book(name_book)
        assert name_book in book.books_genre

    def test_add_new_book_duplicate_name_not_added_again(self):
        book = BooksCollector()
        name_book = 'Отцы и дети'
        book.add_new_book(name_book)
        count_book_first_add = len(book.books_genre)
        book.add_new_book(name_book)
        count_book_second_add = len(book.books_genre)
        assert count_book_first_add == count_book_second_add

    def test_set_book_genre_existing_book_and_valid_genre_updates_successfully(self):
        book = BooksCollector()
        genre = 'Детективы'
        name_book = 'Дом лжи'
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        assert genre in book.genre and name_book in book.books_genre

    def test_set_book_genre_book_exists_but_invalid_genre_not_set(self):
        book = BooksCollector()
        genre = 'Проза'
        name_book = 'Норвежский лес'
        book.add_new_book(name_book)
        assert genre not in book.genre and name_book in book.books_genre

    def test_set_book_genre_genre_exists_but_book_missing_no_update(self):
        book = BooksCollector()
        genre = 'Фантастика'
        name_book = 'Дюна'
        assert genre in book.genre and name_book not in book.books_genre

    @pytest.mark.parametrize('name_book, genre',
                             [['Таинственный остров', 'Фантастика'], ['Оно', 'Ужасы'], ['Дом лжи', 'Детективы'],
                              ['Ёжик в тумане', 'Мультфильмы'], ['Трое в лодке', 'Комедии']])
    def test_get_book_genre_existing_book_returns_correct_genre(self, name_book, genre):
        book = BooksCollector()
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        assert book.books_genre.get(name_book) == genre

    def test_get_books_with_specific_genre_returns_matching_books(self, full_collection_of_books):
        book = full_collection_of_books
        assert book.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_with_specific_genre_empty_dict_returns_empty_list(self):
        book = BooksCollector()
        assert book.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_genre_returns_current_dict(self, full_collection_of_books):
        book = full_collection_of_books
        assert book.get_books_genre() == book.books_genre

    def test_get_books_genre_returns_dict_with_empty_genres(self):
        book = BooksCollector()
        assert book.get_books_genre() == {}

    def test_get_books_for_children_returns_books_without_age_rating(self, full_collection_of_books):
        book = full_collection_of_books
        assert book.get_books_for_children() == ['Таинственный остров', 'Ёжик в тумане', 'Трое в лодке']

    def test_get_books_for_children_no_valid_books_returns_empty_list(self, only_horror_and_detective_collection_of_books):
        book = only_horror_and_detective_collection_of_books
        assert book.get_books_for_children() == []

    def test_get_books_for_children_genre_missing_books_returns_empty_list(self):
        book = BooksCollector()
        book.add_new_book('Оно')
        assert book.get_books_for_children() == []

    @pytest.mark.parametrize('name_book, genre', [('Таинственный остров', 'Фантастика')])
    def test_add_book_in_favorites_valid_book_added_once(self, name_book, genre):
        book = BooksCollector()
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        book.add_book_in_favorites(name_book)
        assert name_book in book.favorites

    @pytest.mark.parametrize('name_book, genre', [('Таинственный остров', 'Фантастика')])
    def test_delete_book_from_favorites_existing_book_removed(self, name_book, genre):
        book = BooksCollector()
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        book.add_book_in_favorites(name_book)
        book.delete_book_from_favorites(name_book)
        assert name_book not in book.favorites

    @pytest.mark.parametrize('name_book, genre', [['Таинственный остров', 'Фантастика']])
    def test_add_book_in_favorites_duplicate_book_ignored(self, name_book, genre):
        book = BooksCollector()
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        book.add_book_in_favorites(name_book)
        count_book_first_add = len(book.favorites)
        book.add_book_in_favorites(name_book)
        count_book_second_add = len(book.favorites)
        assert count_book_first_add == count_book_second_add

    def test_add_book_in_favorites_nonexistent_book_rejected(self):
        book = BooksCollector()
        book.add_book_in_favorites('Ёжик в тумане')
        assert book.favorites == []

    @pytest.mark.parametrize('name_book, genre', [['Таинственный остров', 'Фантастика']])
    def test_delete_book_from_favorites_nonexistent_book_no_change(self, name_book, genre):
        book = BooksCollector()
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        book.add_book_in_favorites(name_book)
        book.delete_book_from_favorites('Ёжик в тумане')
        assert name_book in book.favorites

    @pytest.mark.parametrize('name_book, genre', [('Таинственный остров', 'Фантастика')])
    def test_get_list_of_favorites_books_returns_current_list(self, name_book, genre):
        book = BooksCollector()
        book.add_new_book(name_book)
        book.set_book_genre(name_book, genre)
        book.add_book_in_favorites(name_book)
        assert book.favorites == book.get_list_of_favorites_books()

    @pytest.fixture
    def full_collection_of_books(self):
        book = BooksCollector()
        book.add_new_book('Таинственный остров')
        book.set_book_genre('Таинственный остров', 'Фантастика')
        book.add_new_book('Оно')
        book.set_book_genre('Оно', 'Ужасы')
        book.add_new_book('Дом лжи')
        book.set_book_genre('Дом лжи', 'Детективы')
        book.add_new_book('Ёжик в тумане')
        book.set_book_genre('Ёжик в тумане', 'Мультфильмы')
        book.add_new_book('Трое в лодке')
        book.set_book_genre('Трое в лодке', 'Комедии')
        return book

    @pytest.fixture
    def only_horror_and_detective_collection_of_books(self):
        book = BooksCollector()
        book.add_new_book('Оно')
        book.set_book_genre('Оно', 'Ужасы')
        book.add_new_book('Дом лжи')
        book.set_book_genre('Дом лжи', 'Детективы')
        return book
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()