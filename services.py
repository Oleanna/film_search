import re

from formatter import Formatter
from constants import LIMIT_TOP_SEARCH, RESULTS_PER_PAGE


class Service:
    """
    The Service implements the functionality of searching for films,
    displaying statistics and a list of queries.
    """

    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    @staticmethod
    def display_results(cursor):
        """
         Displays search results page by page.
         The user can choose to display the next page.
        """
        while True:
            results = cursor.fetchmany(RESULTS_PER_PAGE)
            if not results:
                print("Films not found")
                break

            Formatter.print_movies(results)

            if len(results) < RESULTS_PER_PAGE:
                break

            cont = input("For show more, press 'y': ")
            if cont.lower() != "y":
                break

    def search_by_keyword(self):
        """
        Searches films by keyword.
        """
        while True:
            keyword = input("Enter a keyword (or 'q' to quit): ").strip()[:50]
            if keyword.lower() == "q":
                return
            if not keyword:
                print("You didn't enter anything. Please enter a keyword.")
                continue
            break
        cursor = self.db.search_by_keyword(keyword)
        Service.display_results(cursor)
        self.logger.log_search_insert("keyword", {"keyword": keyword})

    def search_by_genre_and_year(self):
        """
        Searches for films by genre and year (or range of years).
        """
        while True:
            genre = input("Enter genre (or 'q' to quit): ").strip()[:50]
            if genre.lower() == "q":
                return
            if not genre:
                print("You didn't enter anything. Please enter a genre.")
                continue
            break
        while True:
            year_input = input("Enter the year or range in YYYY or YYYY-YYYY format (or 'q' to quit): ").strip()
            if year_input.lower() == "q":
                return
            if re.fullmatch(r"\d{4}", year_input):
                year_from = year_to = int(year_input)
                break
            elif re.fullmatch(r"\d{4}-\d{4}", year_input):
                parts = year_input.split("-")
                year_from = int(parts[0].strip())
                year_to = int(parts[1].strip())
                if year_from > year_to:
                    print("Invalid range. The first year should be less than or equal to the second year.")
                    continue
                break
            else:
                print("Invalid input. Please enter a year in YYYY or YYYY-YYYY format.")

        cursor = self.db.search_by_genre_and_year(genre, year_from, year_to)
        Service.display_results(cursor)
        self.logger.log_search_insert("genre_year", {"genre": genre, "year_from": year_from, "year_to": year_to})

    def display_genres_years(self):
        """
        Displays available genres and years.
        """
        print("Available genres and years:")
        results = self.db.search_available_genres_and_years()
        Formatter.print_genres_and_years(results)

    def display_statistics(self):
        """
         Displays statistics on the most popular search requests
        """
        print("Top searches:")
        top_searches = self.logger.top_log_search(LIMIT_TOP_SEARCH)
        Formatter.print_statistics(top_searches)

    def display_last_requests(self):
        """
        Displays a list of the latest search requests.
        """
        print("Last requests:")
        last_requests = self.logger.latest_requests(LIMIT_TOP_SEARCH)
        Formatter.print_last_requests(last_requests)
