import pymysql
import dbconfig


class DBHelper:
    def connect(self, database="crimemap"):
        return pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user=dbconfig.dbUser,
                               passwd=dbconfig.dbPassword,
                               db=database)

    def getAllInputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()


    def addInput(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()


    def clearAll(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()


