from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):
    rating = SelectField('Your rating 1-10', choices=[('1', '1'),
                                                      ('2', '2'),
                                                      ('3', '3'),
                                                      ('4', '4'),
                                                      ('5', '5'),
                                                      ('6', '6'),
                                                      ('7', '7'),
                                                      ('8', '8'),
                                                      ('9', '9'),
                                                      ('10', '10'),])
    review = StringField(label='Your review')
    submit = SubmitField(label='Update review')


class AddMovie(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
