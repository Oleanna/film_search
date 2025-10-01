RESULTS_PER_PAGE = 10
LIMIT_TOP_SEARCH = 5

SEARCH_BY_KEYWORD = """SELECT title, release_year, description
                       FROM film
                       WHERE title LIKE %s
                    """

SEARCH_BY_GENRE_AND_YEAR = """SELECT f.title, f.release_year, c.name AS category, f.description
                              FROM film f
                                       JOIN film_category fc ON f.film_id = fc.film_id
                                       JOIN category c ON fc.category_id = c.category_id
                              WHERE c.name = %s
                                AND f.release_year BETWEEN %s AND %s
                              ORDER BY f.release_year, f.title
                           """

SEARCH_AVAILABLE_GENRE_AND_YEAR = """SELECT c.name              AS category_name,
                                            MIN(f.release_year) AS min_year,
                                            MAX(f.release_year) AS max_year
                                     FROM category c
                                              JOIN film_category fc ON c.category_id = fc.category_id
                                              JOIN film f ON fc.film_id = f.film_id
                                     GROUP BY c.name
                                  """
