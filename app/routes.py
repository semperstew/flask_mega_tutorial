#!/usr/bin/env python

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'semperstew'}
    posts = [
        {
            'author': {'username': 'semperstew'},
            'body': 'Beautiful day in the neighborhood!'
        },
        {
            'author': {'username': 'kwhill'},
            'body': 'I love watching hands make faces!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
