import subprocess
import datetime
import os

DB_HOST = "localhost"
DB_USER = "user"
DB_PASSWORD = "pass"
BACKUP_DIR = "/path/to/your/backup/directory"
DATABASE_NAME = "your_database_name"

def create_backup(db_host, db_user, db_password, db_name, backup_dir):

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{db_name}_backup_{timestamp}.sql"
    backup_filepath = os.path.join(backup_dir, backup_filename)

    mysqldump_command = [
        "mysqldump",
        "-h", db_host,
        "-u", db_user,
        f"--password={db_password}",
        db_name,
        f"--result-file={backup_filepath}"
    ]

    try:
        print(f"Starting backup of database '{db_name}'...")
        subprocess.run(mysqldump_command, check=True)
        print(f"Backup created successfully: {backup_filepath}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating backup: {e}")
    except FileNotFoundError:
        print("Errord")

if __name__ == "__main__":
    os.makedirs(BACKUP_DIR, exist_ok=True)
    create_backup(DB_HOST, DB_USER, DB_PASSWORD, DATABASE_NAME, BACKUP_DIR)
    print("Backup process completed.")