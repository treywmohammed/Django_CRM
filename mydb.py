import mysql.connector 

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Password123$'

	)


# Prepare a cursor object

cursorObject = dataBase.cursor()


# Create a Database

cursorObject.execute("CREATE DATABASE CRM_Build")

print('All Done!')

