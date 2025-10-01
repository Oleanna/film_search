from pymongo import MongoClient
import pymysql
import os
import dotenv
from pathlib import Path
from pymysql.cursors import DictCursor

dotenv.load_dotenv(Path('.env1'))

config = {'host': os.environ.get('host'),
          'user': os.environ.get('user'),
          'password': os.environ.get('password'),
          'database': os.environ.get('database'),
          'charset': 'utf8mb4',
          'cursorclass': DictCursor
          }

mongo_uri = (
    f"mongodb://{os.environ.get('mongo_user')}:{os.environ.get('mongo_password')}@"
    f"{os.environ.get('mongo_host')}/{os.environ.get('mongo_options')}&"
    f"authSource={os.environ.get('mongo_db')}"
)
