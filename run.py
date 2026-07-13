import os
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer

from app.controllers.auth import LoginHandler, LogoutHandler, AdminLoginHandler, AdminLogoutHandler
from app.controllers.home import IndexHandler, AdminIndexHandler
from app.models.db import init_db

def webapp():
    # 定义一个web应用程序，并配置访问各个模块/页面路由
    # 整个程序的安全配置也需要在此处完成
    base_dir = os.path.dirname(os.path.abspath(__file__))
    settings = dict(
        template_path=os.path.join(base_dir, "app", "templates"),
        static_path=os.path.join(base_dir, "app", "static"),
        cookie_secret="datafinderagentos-token",
        login_url="/",
        xsrf_cookies=True,
        debug=True,
        autoreload=True
    )
    return tornado.web.Application([
        # 前台路由
        (r"/", LoginHandler),
        (r"/logout", LogoutHandler),
        (r"/index", IndexHandler),
        # 后台路由
        (r"/admin/", AdminLoginHandler),
        (r"/admin/login", AdminLoginHandler),
        (r"/admin/logout", AdminLogoutHandler),
        (r"/admin/index", AdminIndexHandler)
    ],
    **settings
    )

if __name__ == '__main__':
    init_db()
    webapp = webapp()
    # 将应用程序部署到服务器
    server = HTTPServer(webapp)
    server.listen(10010)
    print("Server Started:http://localhost:10010/", flush=True)
    tornado.ioloop.IOLoop.current().start()