# modules/__init__.py

from models.engine.db_storage import DBStorage

# Create an instance of the DBStorage class
storage = DBStorage()

# Call the reload method to initialize the database
storage.reload()
