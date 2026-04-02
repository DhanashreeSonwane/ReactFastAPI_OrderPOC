import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="orders_db",
        user="dhanashreesonwane",
        password=""   # leave empty if not set
    )
    return conn