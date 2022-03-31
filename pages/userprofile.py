import dominate
from dominate.tags import *

from sanic import Sanic
from config import APP_NAME

from pages.menu import show_menu

def user_profile(user):
    """Helper function for displaying profile info."""
    with div(id='profile-info'):
        h1(user.username)
        img(src=user.img_path)
        p(user.desc)

def edit_profile(user):
    """Full page for editing a user profile."""
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Rediger profil')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))
    
    with doc:
        with div(id='contents'):
            menu_items = [
                ('Forside', '/'),
                ('Log ud', '/logout'),
                ('Ny post', '/write'),
                ('Nyt billede', '/upload'),
            ]
            show_menu(menu_items)
            with form(cls='profile-form', enctype='multipart/form-data', method='POST', action='/update_profile'):
                with div(id='profile-info'):
                    h1(f'{user.username} - rediger profil')
                    img(src=user.img_path)
                    label('Vælg profilbillede:', for_='profile-icon')
                    input_(type='file',
                           name='profile-icon',
                           accept='image/png')
                    textarea(user.desc,
                             cls='desc-inpt',
                             name='description',
                             placeholder='Indtast beskrivelse...')
                    input_(type='submit', value='Gem', cls='button')

    return doc.render()