import pymysql
import constants
from config import config


class MysqlConnector:
    """
     Class to manage MySQL database connections and execute queries.
    """

    def __init__(self):
        """
        Initialize the MySQL connection
        """
        try:
            self.connection = pymysql.connect(**config)
        except pymysql.MySQLError as e:
            print("Service is currently unavailable.")
            self.connection = None

    def execute(self, query, params=None):
        """
        Execute a SQL query with optional parameters.
        """
        if not self.connection:
            print("Service is currently unavailable.")
            return None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            return cursor
        except pymysql.MySQLError as e:
            print("Service is currently unavailable.")
            return None

    def search_by_keyword(self, keyword):
        """
        Search films in the database by keyword.
        """
        return self.execute(constants.SEARCH_BY_KEYWORD, (f'%{keyword}%',))

    def search_by_genre_and_year(self, genre, year_from, year_to):
        """
        Search films by genre and year (or range of years).
        """
        return self.execute(constants.SEARCH_BY_GENRE_AND_YEAR, (genre, year_from, year_to))

    def search_available_genres_and_years(self):
        return self.execute(constants.SEARCH_AVAILABLE_GENRE_AND_YEAR)

    def close(self):
        self.connection.close()
