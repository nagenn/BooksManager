#This is the app that listens to incoming reequests
import tornado.ioloop
import tornado.web

from handlers import (
    MainHandler,
    AddBookHandler,
    ApiBooksHandler,
    LoginHandler,
    LogoutHandler,
)

def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/add", AddBookHandler),
            (r"/api/books", ApiBooksHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
        ],
        template_path="templates",
        static_path="static",
        cookie_secret="VERY_SECRET_KEY",
        debug=True,
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8383)
    print("Server running on http://localhost:8383")
    tornado.ioloop.IOLoop.current().start()
