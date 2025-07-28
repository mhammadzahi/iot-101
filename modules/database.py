import psycopg2
from psycopg2 import sql, OperationalError



def connect_to_db(dbname, user, password, host="localhost", port="5432"):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("✅ Connected to the database")
        return conn
    except OperationalError as e:
        print(f"❌ Connection error: {e}")
        return None

def fetch_all_rows(conn, table_name):
    try:
        with conn.cursor() as cur:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            cur.execute(query)
            return cur.fetchall()
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return []

def insert_row(conn, table_name, data: dict):
    try:
        with conn.cursor() as cur:
            columns = data.keys()
            values = [data[col] for col in columns]
            insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({placeholders})").format(
                table=sql.Identifier(table_name),
                fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
                placeholders=sql.SQL(', ').join(sql.Placeholder() * len(values))
            )
            cur.execute(insert_query, values)
            conn.commit()
            print("✅ Row inserted")
    except Exception as e:
        print(f"❌ Error inserting row: {e}")
        conn.rollback()

def close_connection(conn):
    if conn:
        conn.close()
        print("🔒 Connection closed")
