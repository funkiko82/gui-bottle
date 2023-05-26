#!/usr/bin/env python3

# Homepage
import dominate

from dominate.tags import *
homePage = dominate.document('Welcome to homepage')

with homePage:
    h1('Welcome ' + '{{ user }}', cls='text-center')
    a('Page', href='/')