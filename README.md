# qa_python

    def test_add_new_book_empty_name_not_added(self) - добавление новой книги в словарь с пустым именем

    def test_add_new_book_name_over_forty_chars_rejected(self, name_book)- добавление новой книги в словарь с названием книги больше сорока символов

    def test_add_new_book_valid_value_one_to_forty_chars_added_successfully(self, name_book)- добавление новой книги в словарь с названием книги от одного до сорока символов

    def test_add_new_book_duplicate_name_not_added_again(self) - добавление новой книги в словарь существующей книги

    def test_set_book_genre_existing_book_and_valid_genre_updates_successfully(self) - установка жанра книги если книга есть в словаре и её жанр входит в список

    def test_set_book_genre_book_exists_but_invalid_genre_not_set(self)- установка жанра книги если книга есть в словаре но жанра нет в списке

    def test_set_book_genre_genre_exists_but_book_missing_no_update(self)- установка жанра книги если её жанр входит в список но книга не добавлена в словарь

    def test_get_book_genre_existing_book_returns_correct_genre(self, name_book, genre)- вывод жанра книги по её имени когда словарь заполнен

    def test_get_books_with_specific_genre_returns_matching_books(self, full_collection_of_books)- вывод списока книг с определённым жанром когда словарь заполнен

    def test_get_books_with_specific_genre_empty_dict_returns_empty_list(self) - вывод списока книг с определённым жанром когда словарь пуст

    def test_get_books_genre_returns_current_dict(self, full_collection_of_books) -  вывод текущего словаря когда словарь заполнен

    def test_get_books_genre_returns_dict_with_empty_genres(self) - вывод текущего словаря когда словарь пуст

    def test_get_books_for_children_returns_books_without_age_rating(self, full_collection_of_books) - возврат списка книг, которые подходят детям, с наличием книг в словаре, у которых жанр без возрастного рейтинга 

    def test_get_books_for_children_no_valid_books_returns_empty_list(self, only_horror_and_detective_collection_of_books)  возврат списка книг, которые подходят детям, с отсутствием книг в словаре, у которых жанр без возрастного рейтинга 

    def test_get_books_for_children_genre_missing_books_returns_empty_list(self)  возврат списка книг, которые подходят детям с отсутствием жанра у книг в словаре

    def test_add_and_delete_book_in_favorites_valid_book_added_and_removed(self, name_book, genre) - добавление книги в избранное, когда книга находится в словаре, и удаление добавленной книги из избранного

    def test_add_book_in_favorites_duplicate_book_ignored(self, name_book, genre)  - добавление книги в избранное при попытке повторного добавления книги, которая уже есть в словаре

    def test_add_book_in_favorites_nonexistent_book_rejected(self) - добавление книги в избранное когда у книги в словаре не указан жанр

    def test_delete_book_from_favorites_nonexistent_book_no_change(self, name_book, genre) - удаление книги из избранного, когда книга отсутствует в словаре

    def test_get_list_of_favorites_books_returns_current_list(self, name_book, genre)  -  получение списка избранных книг, если список заполнен


