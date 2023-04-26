# import required libraries and modules
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# creating db instance to provide access to SQLAlchemy functions
db = SQLAlchemy()

migrate = Migrate()

