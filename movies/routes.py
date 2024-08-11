from flask import Flask, render_template, redirect, url_for, request, Blueprint, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, text, desc
from .models import Movie
from . import db
from .forms import RateMovieForm, AddMovie
from .search import MovieSearch
from sqlalchemy.exc import SQLAlchemyError


main = Blueprint('main', __name__)
movie_search = MovieSearch()



@main.route("/")
def home():
    movies = db.session.query(Movie).order_by(desc(Movie.rating)).all()
    if movies[-1].rating != len(movies):
        for movie in range(len(movies)):
            movies[movie].ranking = len(movies) - movie
            db.session.commit()
    return render_template("index.html", movies=movies)


@main.route('/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    form = RateMovieForm()
    movie_to_edit = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        flash('Movie review updated')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.rating.data = movie_to_edit.rating
        form.review.data = movie_to_edit.review
    return render_template('edit.html', form=form, movie_to_edit=movie_to_edit)


@main.route('/delete/<int:movie_id>', methods=['GET', 'POST'])
def delete(movie_id):
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    flash('Movie deleted successfully')
    return redirect(url_for('main.home'))


@main.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        get_movies = movie_search.get_movie(movie_title)
        return render_template('select.html', movies=get_movies, title=movie_title)
    return render_template('add.html', form=form)


@main.route('/fetch')
def fetch():
    movie_id = request.args['id']
    get_movie_data = movie_search.movie_get_data(movie_id)
    try:
        new_movie = Movie(**get_movie_data)
        db.session.add(new_movie)
        db.session.commit()
        movie_database_id = Movie.query.filter_by(title=get_movie_data['title']).first()
        flash('Movie has been added.Please insert ranking of the movie')
        return redirect(url_for('main.edit', movie_id=movie_database_id.id))
    except SQLAlchemyError as error:
        db.session.rollback()
        flash('An error occurred')
        print(f'An error occurred:\n{error}')
        return redirect(url_for('main.home'))

