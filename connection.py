import MySQLdb
from MySQLdb import Error

try:
    connection = MySQLdb.connect(host='localhost',port=3306, database='',user='root',password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
    print("Connected to MySQL database... MySQL Server version on ",db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print ("Your connected to - ", record)
except Error as e :
    print ("Error while connecting to MySQL", e)