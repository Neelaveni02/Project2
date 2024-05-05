import tkinter as tk
from tkinter import ttk, messagebox
from Recommender import Recommender


class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        self.root = tk.Tk()
        self.root.title("Media Recommender")
        self.root.geometry("1200x800")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")

        self.init_movie_tab()
        self.init_tv_tab()
        self.init_book_tab()
        self.init_search_tab()
        self.init_recommendations_tab()


