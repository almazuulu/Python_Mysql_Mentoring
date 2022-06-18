import mysql.connector as mcon
def infoconnection():
    mysqldb_info = mcon.connect(
        host="localhost",
        user="pythonuser",
        password="password12345$",
        database="mysqlLessonMorning"
    )

    return  mysqldb_info

if __name__ == '__main__':
    pass