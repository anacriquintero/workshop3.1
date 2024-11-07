# db_connection.py
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexión a la base de datos establecida.")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    create_table_sql = """CREATE TABLE IF NOT EXISTS predictions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Economy REAL,
                            Family REAL,
                            Health REAL,
                            Freedom REAL,
                            Trust REAL,
                            Generosity REAL,
                            Dystopia REAL,
                            Predicted_Score REAL
                          );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print("Tabla creada.")
    except sqlite3.Error as e:
        print(e)

# Conexión y creación de tabla
conn = create_connection("happiness_predictions.db")
create_table(conn)

