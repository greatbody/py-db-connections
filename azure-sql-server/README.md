# Azure SQL Server Connection Script

This Python script connects to an Azure SQL Server database and executes a simple query.

## Prerequisites

- Python 3.x
- `pyodbc` library
- An Azure SQL Server instance with credentials.
- `dotenvx` CLI installed.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Create a `.env` file** in the root of the project with your database credentials:
    ```env
    SERVER="your_server_name.database.windows.net"
    DATABASE="your_database-name"
    USERNAME="your_username"
    PASSWORD="your_password"
    ```

## Running the script

To run the script, you can use `dotenvx` to load the environment variables from your `.env` file:

```bash
dotenvx run --overload -- python connect.py
```

This command will:
- Load the environment variables defined in your `.env` file.
- Execute the `connect.py` script using the loaded variables.
- The `--overload` flag ensures that variables in the `.env` file take precedence over any existing environment variables with the same names.
