
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class AuthRequiredHandler(BaseHandler):
    def prepare(self):
        if not self.current_user:
            self.redirect("/login")
