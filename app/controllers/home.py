import tornado.web

from app.controllers.base import BaseHandler

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("index.html", title="瞭望与问数首页", username=self.current_user)

class AdminIndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("admin/index.html", title="后台管理", username=self.current_user)