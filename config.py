from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '111602'
app.config['MYSQL_DATABASE_DB'] = 'class_3e'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)