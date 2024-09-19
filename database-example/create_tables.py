from sdrdm_database import DBConnector
from sdrdm_database.dbconnector import SupportedBackends

# Establish a connection to the database
db = DBConnector(
    username="root",
    password="root",
    host="localhost",
    db_name="db",
    port=3306,
    dbtype=SupportedBackends.MYSQL
)

# Create the tables in the database
db.create_tables("../specifications/STRENDADB_light_20240208.md")
