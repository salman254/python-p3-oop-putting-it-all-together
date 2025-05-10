#!/usr/bin/env python3

# lib/book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def __repr__(self):
        return f"Book(title='{self.title}', page_count={self.page_count})"
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or value.strip() == "":
            print("Title must be a non-empty string.")
        else:
            self._title = value
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        elif value <= 0:
            print("Page count must be a positive integer.")
        else:
            self._page_count = value
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
