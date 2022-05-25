from dominate.tags import *

from sanic import Sanic
from config import APP_NAME

def show_menu(menu_items):
    app = Sanic.get_app(APP_NAME)
    with ul(cls='menu'):
        for (fname, lnk) in menu_items:
            with li(cls='menu-item'):
                a(img(cls='menu-icon', 
                      src=app.url_for('static',
                                      name='static',
                                      filename=fname)), cls='button', href=lnk)