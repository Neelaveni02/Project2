from tkinter import filedialog
from Book import Book
from Show import Show


class Recommender:
    def __init__(self):
        self.books_dict = {}
        self.shows_dict = {}
        self.associations_dict = {}

    def load_books(self):
        file_path = filedialog.askopenfilename(title="Open Book File")
        if file_path:
            with open(file_path, 'r') as file:
                headers = file.readline().strip().split('\t')
                for line in file:
                    data = line.strip().split('\t')
                    book_id = data[0]
                    title = data[1]
                    avg_rating = float(data[2])
                    authors = data[3]
                    isbn = data[4]
                    isbn13 = data[5]
                    language_code = data[6]
                    pages = int(data[7])
                    ratings_count = int(data[8])
                    publication_date = data[9]
                    publisher = data[10]
                    book = Book(book_id, title, avg_rating, authors, isbn, isbn13, language_code, pages, ratings_count,
                                publication_date, publisher)
                    self.books_dict[book_id] = book

    def load_shows(self):
        file_path = filedialog.askopenfilename(title="Open Show File")
        if file_path:
            with open(file_path, 'r') as file:
                headers = file.readline().strip().split('\t')
                for line in file:
                    data = line.strip().split('\t')
                    show_id = data[0]
                    title = data[1]
                    avg_rating = float(data[2])
                    show_type = data[3]
                    directors = data[4]
                    actors = data[5]
                    country_code = data[6]
                    added_date = data[7]
                    release_year = int(data[8])
                    rating = data[9]
                    duration = int(data[10])
                    genres = data[11]
                    description = data[12]
                    show = Show(show_id, title, avg_rating, show_type, directors, actors, country_code, added_date,
                                release_year, rating, duration, genres, description)
                    self.shows_dict[show_id] = show

    def load_associations(self):
        file_path = filedialog.askopenfilename(title="Open Associations File")
        if file_path:
            with open(file_path, 'r') as file:
                for line in file:
                    data = line.strip().split('\t')
                    id1 = data[0]
                    id2 = data[1]
                    if id1 not in self.associations_dict:
                        self.associations_dict[id1] = {}
                    if id2 not in self.associations_dict[id1]:
                        self.associations_dict[id1][id2] = 0
                    self.associations_dict[id1][id2] += 1
                    if id2 not in self.associations_dict:
                        self.associations_dict[id2] = {}
                    if id1 not in self.associations_dict[id2]:
                        self.associations_dict[id2][id1] = 0
                    self.associations_dict[id2][id1] += 1

