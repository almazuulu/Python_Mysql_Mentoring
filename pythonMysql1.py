import mysql.connector as mcon
from connectionInfo import infoconnection

# mysqldb_info = mcon.connect(
#     host = "localhost",
#     user = "pythonuser",
#     password = "password12345$",
#     database = "mysqlLessonMorning"
# )

mysqldb_info = infoconnection()

# print(mysqldb_info)

mycursor = mysqldb_info.cursor()

# mycursor.execute("show databases;")
#
# listDatabases = mycursor.fetchall()
#
# # print(type(listDatabases))
# for db in listDatabases:
#     print(db[0])

sqlCreateTable = """
    CREATE TABLE IF NOT EXISTS Djangolessons(
    id int not null primary key auto_increment,
    student_name varchar(100) not null,
    age int,
    country varchar(50)
    );
"""
# mycursor.execute(sqlCreateTable)

sqlInsert = """
INSERT INTO mysqlLessonMorning.Djangolessons(student_name,age,country) VALUES
('Tamara',25,'Poland'),('Maria', 28, 'Ukraine');
"""

# nameStudent  = input("Please input name for student: ")
# age = int(input("Please input age: "))
# country = input("Please input country: ")
#
# sqlInsert2 = f"INSERT INTO mysqlLessonMorning.Djangolessons(student_name,age,country) " \
#             f"VALUES ('{nameStudent}',{age}, '{country}');"

# mycursor.execute(sqlInsert2)

oldName = input("Please input old name: ")
newName = input("Input new name for student: ")

sqlUpdate = f"UPDATE Djangolessons " \
            f"SET student_name = '{newName}' " \
            f"where student_name = '{oldName}'"

mycursor.execute(sqlUpdate)
mysqldb_info.commit()

print('Successfully updated!')







