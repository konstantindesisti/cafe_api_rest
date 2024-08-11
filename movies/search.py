import requests
from dotenv import load_dotenv
import os
import json


class MovieSearch:
    load_dotenv()
    API_KEY = os.getenv('THEMOVIEDB_API_KEY')
    endpoint = 'https://api.themoviedb.org/3'
    headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {API_KEY}'
    }

    def get_movie(self, movie_title):
        """
        Searches TheMovieDB for movie by provided title

        :param movie_title: Title of movie you want to search
        :return: json which contains matched results
        """

        movie_params = {
            'query': movie_title
        }
        response = requests.get(url=f'{self.endpoint}/search/movie', headers=self.headers, params=movie_params).json()
        movie_list = response['results']
        return movie_list

    def movie_get_data(self, movie_id: int):
        """
        Gets information of selected movie
        :param movie_id: ID for searching https://developer.themoviedb.org/reference/movie-details
        :return: All info of movie which can be inserted in db
        """
        movie_params = {
            'movie_id': movie_id
        }
        response = requests.get(url=f'{self.endpoint}/movie/{movie_id}', headers=self.headers, params=movie_params).json()
        base_poster_path = 'https://image.tmdb.org/t/p/'
        poster_size = 'w500'
        poster_path = response['poster_path']
        movie_data = {
            'title': response['original_title'],
            'img_url': f'{base_poster_path}{poster_size}{poster_path}',
            'year': int(response['release_date'].split('-')[0]),
            'description': response['overview'],
            'rating': response['vote_average'],
            'review': response['tagline'],
            'ranking': 5
        }
        return movie_data



