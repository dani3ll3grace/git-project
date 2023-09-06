from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/test_db_connection')
def test_db_connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='111602',
            db='class_3e'
        )
        # Perform a simple database query to test the connection
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return "Connected to the database successfully."
        else:
            return "Failed to connect to the database."
    except Exception as e:
        return f"Database connection error: {str(e)}"

if __name__ == '__main__':
    app.run()
