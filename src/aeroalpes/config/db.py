from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = None

DB_USERNAME = os.getenv('DB_USERNAME', default='root')
DB_PASSWORD = os.getenv('DB_PASSWORD', default='adminadmin')
DB_HOSTNAME = os.getenv('DB_HOSTNAME', default='localhost')
DB_ENGINE = os.getenv('DB_ENGINE', default='mysql')

class DatabaseConfigException(Exception):
    def __init__(self, message='Configuration file is Null or malformed'):
        self.message = message
        super().__init__(self.message)


def database_connection(config, basedir=os.path.abspath(os.path.dirname(__file__))) -> str:
    if not isinstance(config,dict):
        raise DatabaseConfigException

    if DB_ENGINE == 'sqlite' or config.get('TESTING', False) == True:
        return f'sqlite:///{os.path.join(basedir, "database.db")}'
    else:
        return f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/reservas'


def init_db(app: Flask):
    global db 
    db = SQLAlchemy(app)
