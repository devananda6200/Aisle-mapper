import os

class Config:
    # Set the SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///aisle_mapper.db'  # Relative path to the database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance
