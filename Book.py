from Media import Media


class Book(Media):
    def __init__(self, media_id, title, avg_rating, authors, isbn, isbn13, language_code, pages, ratings_count,
                 publication_date, publisher):
        super().__init__(media_id, title, avg_rating)
        self._authors = authors
        self._isbn = isbn
        self._isbn13 = isbn13
        self._language_code = language_code
        self._pages = pages
        self._ratings_count = ratings_count
        self._publication_date = publication_date
        self._publisher = publisher

    def get_authors(self):
        return self._authors

    def set_authors(self, authors):
        self._authors = authors

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    def get_isbn13(self):
        return self._isbn13

    def set_isbn13(self, isbn13):
        self._isbn13 = isbn13

    def get_language_code(self):
        return self._language_code

    def set_language_code(self, language_code):
        self._language_code = language_code

    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        self._pages = pages

    def get_ratings_count(self):
        return self._ratings_count

    def set_ratings_count(self, ratings_count):
        self._ratings_count = ratings_count

    def get_publication_date(self):
        return self._publication_date

    def set_publication_date(self, publication_date):
        self._publication_date = publication_date

    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._publisher = publisher

