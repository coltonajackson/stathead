import os, sys, importlib, sqlite3

if __name__ == "__main__":
    # Set sys.argv[1] to the league
    league = sys.argv[1]

    # Import schema based on league
    module_path = os.path.join(league, "schemas")
    module_name = module_path.split('.')[0].replace('\\', '.')
    schemas = importlib.import_module(module_name)

    # Set db to the .db file for the league
    db = os.path.join(league, f"{league}.db")

    # Create a connection to the database (or create it if it doesn't exist)
    conn = sqlite3.connect(db)

    # Create a cursor object
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.executescript(schemas.SCHEMA_SCRIPT)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()