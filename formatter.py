from prettytable import PrettyTable


class Formatter:

    @staticmethod
    def print_movies(films):
        if not films:
            print("No results")
            return
        table = PrettyTable()
        table.field_names = ["Title", "Year", "Description"]

        table.align["Title"] = "l"
        table.align["Year"] = "c"
        table.align["Description"] = "l"

        table.max_width["Title"] = 40
        table.max_width["Description"] = 100
        for i, row in enumerate(films, start=1):
            table.add_row([row["title"], row["release_year"], row["description"]])
        print(table)

    @staticmethod
    def print_genres_and_years(films):
        if not films:
            print("No results")
            return
        for i, row in enumerate(films, start=1):
            print(f"{row["category_name"]:<12} {row["min_year"]:>8} - {row["max_year"]:<8}")

    @staticmethod
    def print_statistics(request):

        for i, r in enumerate(request, start=1):
            search_type = r["_id"]["search_type"]
            params = r["_id"]["params"]

            if search_type == "keyword":
                text_request = params["keyword"]
                type_search = "by keyword:"
            elif search_type == "genre_year":
                type_search = "by genre and year:"
                genre = params.get("genre", "Unknown")
                year_from = params.get("year_from")
                year_to = params.get("year_to")

                if year_from == year_to:
                    text_request = f"{genre} {year_from}"
                else:
                    text_request = f"{genre} {year_from} - {year_to}"
            else:
                text_request = str(params)

            print(f"{i:^3} {type_search:<20} {text_request:<40}")

    @staticmethod
    def print_last_requests(requests):
        for i, r in enumerate(requests, start=1):
            type_search = r.get("search_type", "Unknown")
            params = r.get("params", {})

            if type_search == "genre_year":
                search_type = "by genre and year"
                genre = params.get("genre", "Unknown")
                year_from = params.get("year_from")
                year_to = params.get("year_to")

                if year_from and year_to:
                    if year_from == year_to:
                        text_request = f"{genre} {year_from}"
                    else:
                        text_request = f"{genre} {year_from} - {year_to}"
                else:
                    text_request = genre
            else:
                search_type = "by keyword"
                text_request = params.get("keyword", "Unknown")

            print(f"{i:^3} {search_type:<20}: {text_request:<40}")
