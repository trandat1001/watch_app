import sqlite3

class DBConnection:
    
    connection = None

    @staticmethod
    def getConnection():
        if (DBConnection.connection is None):
            DBConnection.connection = sqlite3.Connection(r"data/db_Watch.db")
        
        return DBConnection.connection
    
    @staticmethod
    def execute(sqlStr, params = {}):
        connection = DBConnection.getConnection()
        result = connection.execute(sqlStr, params)
        
        return result

    @staticmethod
    def fetchAll(sqlStr, params = {}):
        connection = DBConnection.getConnection()
        cur = connection.execute(sqlStr, params)

        return cur.fetchall()
    
    @staticmethod
    def fetchOne(sqlStr, params = {}):
        connection = DBConnection.getConnection()
        cur = connection.execute(sqlStr, params)

        return cur.fetchone()

    @staticmethod
    def commit():
        connection = DBConnection.getConnection()

        return connection.commit()

    @staticmethod
    def close():
        DBConnection.getConnection().close()

        return
    

