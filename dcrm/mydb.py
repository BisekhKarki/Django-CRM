# Install MYSQL on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import pymysql

# Connect to MySQL
dataBase = pymysql.connect(
        host='localhost',
        user='root',      # Replace 'root' if using a different username
        passwd='12345',   # Replace '12345' with your MySQL root password
    )
print("Connection to MySQL successful.")

    # Prepare a cursor object
cursorObject = dataBase.cursor()

    # Create a new database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")
print("Database 'elderco' created successfully.")
