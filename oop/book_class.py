# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initialize the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for debugging/recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
