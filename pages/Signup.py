import dominate
from dominate.tags import *

from sanic import Sanic
from config import APP_NAME

def signup_page():
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | register')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))

        with div(cls='login_box2'):
            if app.ctx.msg:
                p(app.ctx.msg, cls='login_err')
                app.ctx.msg = ""
            with div(cls='login_col'):
                with form(method='POST', action='/register'):
                    with div(cls='login_row'):
                        label('Brugernavn:', for_='username')
                        input_(type='text', id='username', name='uname')
                    with div(cls='login_row'):
                        label('Adgangskode:', for_='password')
                        input_(type='password', id='password', name='pword')
                    with div(cls='login_row'):
                        label('Gentag adgangskode:', for_='rpassword')
                        input_(type='password', id='rpassword', name='rpword')
                    with div(cls='login_row'):
                        input_(value='Registrer', type='submit', cls='button')

    return doc.render()