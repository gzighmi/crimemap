import crimeMap.dbHelper as dbHelper
import crimeMap.dbconfig as dbconfig
import pymysql



def connect(database="crimemap"):
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user=dbconfig.dbUser,
                           passwd=dbconfig.dbPassword,
                           db=database,
                           server_public_key=None)


def getAllInputs():
    connection = connect()
    try:
        query = "SELECT description FROM crimes;"
        with connection.cursor() as cursor:
            cursor.execute(query)
        return cursor.fetchall()
    finally:
        connection.close()


def addInput(data):
    connection = connect()
    try:
        query = "INSERT INTO crimes (description) VALUES('{}');".format(data)
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()


def clearAll():
    connection = connect()
    try:
        query = "DELETE FROM crimes;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()


print(getAllInputs())