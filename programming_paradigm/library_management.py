class Book:
    def __init__(self, title, author):
        self.title = title          # public attribute
        self.author = author        # public attribute
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # was not checked out

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                else:
                    return f"'{title}' is already checked out."
        return f"Book '{title}' not found."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned."
                else:
                    return f"'{title}' was not checked out."
        return f"Book '{title}' not found."

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
            return

        for book in available_books:
            print(f"{book.title} by {book.author}")
