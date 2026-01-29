import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        # To-Do: إضافة الاتصال لقاعدة البيانات
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    # To-Do: إرجاع الاتصال 
    return conn

def close_connection(conn):
    """ closes a connection to a database """
    conn.close()

def select_all(conn):
    """select all rows from our table using the conn we already created """
    cur = conn.cursor()
    # To-Do: كتابة استعلام SQL لجلب كل البيانات من جدول longley
    query = "SELECT * FROM longley"

    cur.execute(query)

    # To-Do: جلب كل الصفوف باستخدام الـ cursor (cur)
    rows = cur.fetchall()

    return rows 

def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    for row in rows:
        print(row)