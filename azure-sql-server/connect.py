import sys
import pyodbc # Keep pyodbc for database connection
from dataclasses import dataclass
import os

@dataclass
class DatabaseConfig:
    server: str
    database: str
    username: str
    password: str

    def get_connection_string(self) -> str:
        # Ensure you have the ODBC driver installed, e.g., ODBC Driver 17 for SQL Server
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"

def connect_to_database(config: DatabaseConfig) -> pyodbc.Connection:
    """Establish connection to the Azure SQL database."""
    try:
        print(f"Connecting to database: {config.server}/{config.database}")
        # print(f"Using connection string: {config.get_connection_string()}") # Optional: for debugging
        conn = pyodbc.connect(config.get_connection_string())
        print(f"Successfully connected to the database!")
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {str(e)}")
        sys.exit(1)

def main():
    conn = None  # Initialize conn to None
    try:
        # Load database configuration from environment variables
        server = os.getenv('SERVER')
        database = os.getenv('DATABASE')
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        if not all([server, database, username, password]):
            print("Error: Database configuration environment variables (SERVER, DATABASE, USERNAME, PASSWORD) not set.")
            sys.exit(1)

        config = DatabaseConfig(server, database, username, password)

        # Connect to the database
        conn = connect_to_database(config)

        # Create a cursor
        cursor = conn.cursor()

        # Execute the query "select 1"
        print(f"\nExecuting query: 'SELECT 1'")
        cursor.execute("SELECT 1")

        # Fetch and print the result
        result = cursor.fetchone()
        if result:
            print(f"Query result: {result[0]}")
        else:
            print(f"Query executed, but no result was returned.")

        cursor.close()

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if conn: # Check if conn was successfully assigned
            conn.close()
            print(f"\nDatabase connection closed.")

if __name__ == "__main__":
    main()