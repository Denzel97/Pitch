# from flask import render_template
from flask_login import login_required
from . import main

from flask import Flask, render_template

# Views
# @main.route('/register')
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/login')
def sign_in():

    return render_template('login.html')


# @app.route('/pitch/pitch/new/<int:id>', methods = ['GET','POST'])

# def new_pitch(id):
#     form = ReviewForm()

#     movie = get_movie(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data

#         new_review = Review(movie.id,title,movie.poster,review)
#         new_review.save_review()

#         return redirect(url_for('movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_review.html',title = title, review_form=form, movie=movie)
