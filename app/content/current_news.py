"""
    File that contain class of current news
"""
from os import getenv
import requests

class CurrentNews():
    """
    Class that contain functions to get data from CurrentApi
    """

    def __init__(self, language='en', region='us') -> None:
        self.api_key = getenv('API_KEY')
        self.base_path = 'https://api.currentsapi.services/v1/latest-news?'
        self.language = language
        self.region = region
        self.api_url = None

    def get_url(self) -> str:
        """
        Method that set the api_url to initiate the class
        """
        self.api_url = f'{self.base_path}language={self.language}&apiKey={self.api_key}'

    def get_news(self):
        """
        Method that get data from currentapi
        Return: List of news
        """
        return requests.get(url=self.api_url, timeout=4).json()
