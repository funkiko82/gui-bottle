#!/usr/bin/env python3
# Signup page
import random

import dominate
from dominate.tags import *

signUp = dominate.document('Sign Up')

# Directory of stylesheet
bootswatch = '/static/css/'

bootstrap = '/static/js/'

# JavaScript library file
jscript = ['jquery-3.4.1', 'popper.min', 
           'bootstrap.bundle', 'bootstrap', 
            'scrollax.min', 'owl.carousel.min']
            
with signUp.head:
# Use list comprehension to make it concise, readable and pythonic
    [link(rel='stylesheet', href=bootswatch + i + '.css') 
     for i in ('litera5', 'mystyle')]
#    Ditch this.
#    link(rel='stylesheet', 
#         href=bootswatch + 'litera5.css')
#    link(rel='stylesheet', 
#         href=bootswatch + 'mystyle.css')
    [script(src=bootstrap + x + '.js' ) for x in jscript]


with signUp:
    with div(cls='container'):
        with h1():
            img(src='/static/fonts/icons/logo-python.svg',
                heigth=80, 
                width=80)
            span('Awesome Python', 
                 cls='text-warning')
        with div(cls='row'):
           # admonish section
            with div(cls='col-md-7'):
                pic = ['bebrave', 'havefaith']
                nextpic = random.choice(pic)
                img(src='/static/imgs/'+ nextpic +'.png', 
                    style='background-size: cover; \
                           background-repeat: no-repeat;', 
                    heigth=500,
                    width=500)  
           # Sign up section
            with div(cls='col-md-5'):
                with div(cls='container', 
                         style='border:2px solid gray; \
                                border-radius:15px 15px 0px 0px;'):
                    with form(action='/signup', 
                              method='post', 
                              cls='form form-group'):
                        img(src='/static/fonts/icons/person-circle-outline.svg', 
                            heigth=80, 
                            width=80)
                        span('Sign Up')
                        with div(cls='form-floating mb-3'):
                            input(name="username",
                                  type='username', 
                                  cls='form-control', 
                                  placeholder='Email/Username')
                            label('Username')
                        with div(cls='form-floating'):
                            input(name="password",
                                  type='password', 
                                  cls='form-control', 
                                  placeholder='Password')
                            label('Password')
                            with div(cls='row'):
                                span('{{ error }}', cls='col text-warning')
                        button('Continue', cls='btn btn-secondary btn-lg-12 \
                                                btn-block mb-2 m-2 p-2', 
                                           name='continue', 
                                           style='width: 100%',
                                           type='submit')
                        a('Login', href='/')
            
