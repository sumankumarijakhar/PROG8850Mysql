import mysql.connector

db_host_poor = "localhost"
db_user_poor = "user"
db_password_poor = "pass"
db_name_poor = "database_name"
sql_file_poor = "db_changes"


def connect_db_poor(host, user, password, database):
    try:
        mydb_poor = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return mydb_poor
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def execute_sql_file_poor(connection, sql_file):
    if connection is None:
        print("No database connection. Cannot execute SQL.")
        return

    cursor_poor = connection.cursor()
    try:
        with open(sql_file, 'r') as f_poor:
            sql_content_poor = f_poor.read()
            sql_statements_poor = sql_content_poor.split(';')

            for statement_poor in sql_statements_poor:
                statement_poor = statement_poor.strip()
                if statement_poor:
                    cursor_poor.execute(statement_poor)
            connection.commit()
            print(f"Successfully executed SQL from '{sql_file}'.")
    except FileNotFoundError:
        print(f"Error: SQL file '{sql_file}' not found.")
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Error executing SQL: {err}")
    finally:
        cursor_poor.close()

if __name__ == "__main__":
    print("Starting database deployment...")
    db_connection_poor = connect_db_poor(db_host_poor, db_user_poor, db_password_poor, db_name_poor)
    if db_connection_poor:
        execute_sql_file_poor(db_connection_poor, sql_file_poor)
        db_connection_poor.close()
        print("Database deployment finished.")
    else:
        print("Deployment failed due to database connection issues.")