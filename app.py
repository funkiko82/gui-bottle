#!/usr/bin/env python3

# A Modern Desktop Application in Python
# Built with Cool Python libraries.
# Dominate - A python library for creating and manipulating HTML documents
#            using elegant DOM api.
# Bottle - A lightweigth python no external dependencies web framework.
# Pywebview - Lets you build GUI for python using HTML, CSS and Javascript
#             web technology. A ligthweigth electron for python.
# Author:Francis Cometa
# Started the project May 6,2023

# Core library
import sqlite3
# Third-party library
from bottle import (run, route, template, redirect,
                    debug, get, static_file, request)
import webview
import bcrypt
# Local library
from quotes import quote, verse
from home_page import homePage
from signup import signUp
from index import index, info


# Route pages for our desktop app
@route('/')
@route('/index', method='GET')
def root():
    return template(str(index), q=quote, v=verse, i=info, fail='')
    
@route('/index', method='POST')
def root_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    connection = sqlite3.connect('user_credentials.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT password
        FROM users
        WHERE username = ?;
    ''', (username,))

    result = cursor.fetchone()

    if result is not None:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), 
                                        bcrypt.gensalt())
        # Verify the password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            redirect('/home/' + str(username))
    return template(str(index), q=quote, v=verse, 
                                i=info, fail='Login Failed')
    

@route('/home/<user>')
def homepage(user):
        
    return template(str(homePage), user=user)

@route('/signup', method='GET')
def signup_page():
    return template(str(signUp), error='')
    
    
@route('/signup', method='POST')
def signup_submit():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    connection = sqlite3.connect('user_credentials.db')
    cursor = connection.cursor()
    try:
        # Save the newly registered user information into the database
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        connection.commit()
        redirect('/index')
    except sqlite3.IntegrityError:
        return template(str(signUp), error="Username already exists")
#    return template(str(signUp))

# Serving static assets files for my application
@get('/static/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff)>')
def fonts(filepath):
    return static_file(filepath, root='static/fonts')

@get('/static/imgs/<filepath:re:.*\.(png|jpg|jpeg|svg)>')
def img(filepath):
    return static_file(filepath, root='static/imgs')

@get('/static/css/<filepath:re:.*\.css>')
def css(filepath):
    return static_file(filepath, root='static/css')

@get('/static/css/<filepath:re:.*\.css>')
def mycss(filepath):
    return static_file(filepath, root='static/css')

@get('/static/js/<filepath:re:.*\.js>')
def js(filepath):
    return static_file(filepath, root='static/js')

@get('/static/video/<filepath:re:.*\.mp4>')
def video(filepath):
    return static_file(filepath, root='static/video')


if __name__ == '__main__':
    import threading
    thread = threading.Thread(
        target=run, 
        kwargs=dict(host='localhost', 
                    port=8000), 
                    daemon=True)
    thread.start()
#    run(reloader=True)
    print(index)
    webview.create_window('Dominate', 
        'http://localhost:8000', 
        width=1000, 
        height=860, 
        resizable=True)
    # GUI=['gtk', 'qt']
    webview.start(debug=True, gui='qt' )
