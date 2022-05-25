from urllib.parse import quote
import dominate
from dominate.tags import *

from sanic import Sanic
from config import APP_NAME

import pages.userprofile as userprofile
from pages.menu import show_menu
import database.post as post

def show_posts(posts=[], user=None):
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Posts')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))
        link(rel='stylesheet', href='https://use.typekit.net/yzl7wku.css')

    with doc:
        menu_items = [
            ('Home icon.png', '/'),
            ('Log out icon.png', '/logout'),
            ('New post icon.png', '/write'),
            ('New post icon.png', '/upload'),
            ('Venner icon.png', '/profile'),
            ('search icon.png', '/')
        ]
        with div(cls='header'):
            show_menu(menu_items)
        if user is not None:
            userprofile.user_profile(user)
        for display_post in posts:
            with div(cls='content'):
                if isinstance(display_post.post, post.TextPost): # text post
                    with div(cls='author-text'):
                        a(f'{display_post.author.username}',
                            href=f'/u/{quote(display_post.author.username)}',
                            cls='author_link')
                    with div(cls='post-txt'):
                        h1(display_post.post.title)
                        lines = filter(bool, display_post.post.contents.splitlines())
                        for par in lines:
                            p(par)
                    with div(cls='comment-box'):
                        p('comment...')
                        
                else: # image post
                    with div(cls='post'):
                        with div(cls='image'):
                            img(src=app.url_for('static',
                                                name='static',
                                                filename=f'images/posts/{display_post.post.image_path}'))
                    with div(cls='comment-box'):
                        with div(cls='author'):
                            a(f'{display_post.author.username}',
                                href=f'/u/{quote(display_post.author.username)}',
                                cls='author_link')
                            h1(display_post.post.title)
                        with div(cls='comment'):
                            p('comment...')
    return doc.render()

def create_image_page():
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Upload billede')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))

    with doc:
        menu_items = [
            ('Forside', '/'),
            ('Log ud', '/logout'),
            ('Ny post', '/write'),
            ('Rediger profil', '/profile')
        ]
        show_menu(menu_items)
        with form(cls='post-form', enctype='multipart/form-data', method='POST', action='/post/image'):
            with div(cls='post'):
                input_(type='text', cls='title_inp',
                        name='title',
                        placeholder='Indtast titel...')
                input_(type='file', name='image', accept='image/*')
            input_(type='submit', value='Post', cls='button')

    return doc.render()

def create_page():
    app = Sanic.get_app(APP_NAME)
    doc = dominate.document(title=f'{APP_NAME} | Skriv')

    with doc.head:
        link(rel='stylesheet', href=app.url_for('static',
                                                name='static',
                                                filename='style.css'))

    with doc:
        menu_items = [
            ('Forside', '/'),
            ('Log ud', '/logout'),
            ('Nyt billede', '/upload'),
            ('Rediger profil', '/profile')
        ]
        show_menu(menu_items)
        with form(cls='post-form', method='POST', action='/post/text'):
            with div(cls='post'):
                input_(type='text', cls='title_inp',
                        name='title',
                        placeholder='Indtast titel...')
                textarea(cls='contents_inp',
                            name='contents',
                            placeholder='Indtast tekst...')
            input_(type='submit', value='Post', cls='button')

    return doc.render()