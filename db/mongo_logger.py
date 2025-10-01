from datetime import datetime, timezone
import os
import pymongo
from pymongo.errors import PyMongoError

from config import mongo_uri


class MongoLogger:
    """
    Class for logging search requests in MongoDB.
    Saves requests and allows you to get statistics.
    """

    def __init__(self):
        """
        Initialise connection to MongoDB.
        """
        try:
            client = pymongo.MongoClient(mongo_uri)
            db = client[os.environ.get('mongo_db')]
            self.collection = db[os.environ.get('mongo_collection')]
        except PyMongoError as e:
            print(f"Failed to connect to MongoDB: {e}")
            self.collection = None

    def log_search_insert(self, search_type, params):
        """
        Logs a new search request to the database.
        """
        log = {
            "timestamp": datetime.now(timezone.utc),
            "search_type": search_type,
            "params": params
        }
        try:
            self.collection.insert_one(log)
        except PyMongoError as e:
            print(e)

    def top_log_search(self, limit):
        """
        Returns the most popular search requests.
        """
        pipeline = [
            {"$group": {"_id": {"search_type": "$search_type", "params": "$params"}, "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": limit}
        ]
        try:
            return self.collection.aggregate(pipeline)
        except PyMongoError as e:
            print(f"Service is currently unavailable.")
            return []

    def latest_requests(self, limit):
        """
        Returns the latest search requests.
        """
        pipeline = [
            {"$sort": {"timestamp": -1}},
            {"$limit": limit},
            {"$project": {"_id": {"search_type": "$search_type", "params": "$params"}}}
        ]
        try:
            return self.collection.aggregate(pipeline)
        except PyMongoError as e:
            print(f"Service is currently unavailable.")
            return []

    def close(self):
        self.collection.database.client.close()
