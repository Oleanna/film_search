# Film Search App

Application for searching films by keywords, genres, and years, with statistics on requests stored.

## Functionality
- Search for films by keywords  
- Search for films by genre and year (or range of years)  
- View statistics:
  - Top popular requests
  - Latest requests  
- Statistics on requests are stored in MongoDB 
- Films data is stored in MySQL 

## Requirements
- Python 3.10+
- MySQL
- MongoDB

## Installation
- Clone the repository
- Install dependencies -- `pip install -r requirements.txt`

### Configuration

Create a .env file in the project root with connection parameters:

Copy code:
```host=localhost
user=root
password=your_password
database=movies

mongo_user=root
mongo_password=your_password
mongo_host=localhost
mongo_db=movies_logs
mongo_collection=search_logs
mongo_options=DEFAULT
```

- In config.py, read the environment variables:


```sh
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
```

## Start
film_search_app.py

# Project structure
```sh
project/
│── db/
│   ├── mysql_connector.py
│   └── mongo_logger.py
│── services.py
│── constants.py
│── config.py
│── main.py
│── README.md
│── requirements.txt
```