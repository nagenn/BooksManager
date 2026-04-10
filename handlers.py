
import tornado.web
import json

from models import get_all_books, add_book, authenticate
from auth import BaseHandler, AuthRequiredHandler
from db import init_db


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        user = authenticate(username, password)

        if user:
            self.set_secure_cookie("user", username)
            self.redirect("/")
        else:
            self.write("Invalid credentials")


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")


class MainHandler(AuthRequiredHandler):
    def get(self):
        #books = get_all_books()
        books = [dict(b) for b in get_all_books()]

        self.render("index.html", books=books)


class AddBookHandler(AuthRequiredHandler):
    def get(self):
        self.render("add.html")

    def post(self):
        title = self.get_argument("title")
        author = self.get_argument("author")

        add_book(title, author)

        self.redirect("/")


class ApiBooksHandler(AuthRequiredHandler):
    def get(self):
        #books = get_all_books()
        books = [dict(b) for b in get_all_books()]

        result = []

        for book in books:
            result.append(dict(book))

        self.write(json.dumps(result))


init_db()
