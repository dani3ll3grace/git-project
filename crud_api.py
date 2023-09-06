import pymysql
import pymysql.cursors
from cryptography.fernet import Fernet
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

<<<<<<< HEAD
=======
movies = [
    {"id": 1, "title": "Spirited Away", "director": "Hayao Miyazaki", "release_year": 2001, "genre": "Adventure"},
    {"id": 2, "title": "A Silent Voice", "director": "Naoko Yamada", "release_year": 2016, "genre": "Drama"},
    {"id": 3, "title": "The Girl Who Lept Through Time", "director": "Mamoru Hosoda", "release_year": 2006, "genre": "Sci-Fi"},
    {"id": 4, "title": "Arriety", "director": "Hiromasa Yonebayashi", "release_year": 2010, "genre": "Fantasy"},
    {"id": 5, "title": "Your Name", "director": "Makoto Shinkai", "release_year": 2016, "genre": "Romance"},
]
#####################3
@app.route('/create', methods=['POST'])
def create_emp():
    try:        
        _json = request.json
        id = _json['id']
        first_name = _json['first_name']
        last_name = _json['last_name']
        grade = _json['grade']
        class_number = _json['class_number']
        birthday = _json['birthday']
        if id and first_name and last_name and grade and class_number and birthday and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO student (id, first_name, last_name, grade, class_number, birthday) VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (id, first_name, last_name, grade, class_number, birthday)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Student added successfully!')
            respone.status_code = 200
            return respone
        else:
            return jsonify['Error']
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()    
>>>>>>> 5bd3982f3f3bcf4675007197ff157a65dd0242f2

# Create Student
@app.route('/create', methods=['POST'])
def createStudent():
    try:        
        _json = request.json
        id = _json['id']
        first_name = _json['first_name']
        last_name = _json['last_name']
        grade = _json['grade']
        class_number = _json['class_number']
        birthday = _json['birthday']
        if id and first_name and last_name and grade and class_number and birthday and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO student (id, first_name, last_name, grade, class_number, birthday) VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (id, first_name, last_name, grade, class_number, birthday)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Student added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# All Students View
@app.route('/student', methods=['GET'])
def students():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM student")
        studentRows = cursor.fetchall()
        respone = jsonify(studentRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


# Select Student View
@app.route('/student/<int:id>')
def students_details(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM  student WHERE id = %s", id)
        studentRows = cursor.fetchone()
        respone = jsonify(studentRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


# Update Student Data (Still Editing)
@app.route('/update', methods=['PUT'])
def update_student():
    try:
        _json = request.json
        id = _json['id']
        first_name = _json['first_name']
        last_name = _json['last_name']
        grade = _json['grade']
        class_number = _json['class_number']
        birthday = _json['birthday']
        if id and first_name and last_name and grade and class_number and birthday and request.method == 'PUT':			
            sqlQuery = "UPDATE student SET id=%s, first_name=%s, last_name=%s, grade=%s, class_number=%s, birthday=%s WHERE id=%s"
            bindData = (id, first_name, last_name, grade, class_number, birthday,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Student updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 



@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_student(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM student WHERE id =%s", (id,))
		conn.commit()
		respone = jsonify('Student deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


# Error Handler
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record does not exist: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == '__main__':
    app.run()