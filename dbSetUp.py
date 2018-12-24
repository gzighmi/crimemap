import pymysql
import crimeMap.dbconfig as dbconfig

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user=dbconfig.dbUser,
                             password=dbconfig.dbPassword,
                             server_public_key=None)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
        id int NOT NULL AUTO_INCREMENT,
        lattitude FLOAT(10,6),
        longitude FLOAT(10,6),
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(1000),
        updatedAt TIMESTAMP,
        PRIMARY KEY (id)
        )"""
        cursor.execute(sql);
    connection.commit()
finally:
    connection.close()