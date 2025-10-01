from db.mysql_connector import MysqlConnector
from db.mongo_logger import MongoLogger
from constants import LIMIT_TOP_SEARCH
from services import Service

db = MysqlConnector()
logger = MongoLogger()
service = Service(db, logger)


def display_statistic_menu():
    """
    Displays the statistics menu and processes the user's selection.
    """
    print("-" * 30)
    print("STATISTICS MENU")
    print("-" * 30)
    print(f"1. The top {LIMIT_TOP_SEARCH} most popular requests")
    print(f"2. Last {LIMIT_TOP_SEARCH} search requests")
    print("3. Back to main menu")
    stat_choice = input("Select an option: ")

    if stat_choice == "1":
        service.display_statistics()
    elif stat_choice == "2":
        service.display_last_requests()
    elif stat_choice == "3":
        return
    else:
        print("Invalid selection")


def menu():
    """
    Displays the main menu of the application and processes user selections.
    """
    database = MysqlConnector()

    while True:
        print("-" * 30)
        print("MENU")
        print("-" * 30)
        print("1. Search by keyword")
        print("2. Search by genre and year")
        print("3. Display statistics")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            service.search_by_keyword()
        elif choice == "2":
            service.display_genres_years()
            service.search_by_genre_and_year()
        elif choice == "3":
            display_statistic_menu()
        elif choice == "4":
            print("Exit")
            database.close()
            logger.close()
            break
        else:
            print("Invalid selection")



