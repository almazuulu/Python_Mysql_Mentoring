import mysql.connector as mcon
from connectionInfo import infoconnection

mysqldb_info = infoconnection()
mycursor = mysqldb_info.cursor()


def deleteStudent():
    userName = input('Please input student name to delete: ')
    sqlDelete = f"""
    DELETE FROM Djangolessons 
    where student_name = '{userName}';
    """

    mycursor.execute(sqlDelete)
    mysqldb_info.commit()

def insertStudent():
    userName = input('Please enter the name to insert: ')
    age = int(input('Please enter the age: '))
    country = input('Please enter the country: ')
    sqlInsert = f"""
            INSERT INTO Djangolessons(student_name,age,country) 
            VALUES ('{userName}', {age}, '{country}');
            """

    mycursor.execute(sqlInsert)
    mysqldb_info.commit()
    print('Successfully inserted!')

def updateStudent():
    oldName = input('Please enter old name: ')
    newName = input('Please enter the name to update: ')
    sqlUpdate = f"UPDATE Djangolessons " \
                f"SET student_name = '{newName}' " \
                f"where student_name = '{oldName}'"

    mycursor.execute(sqlUpdate)
    mysqldb_info.commit()
    print('Successfully updated!')

def showAllStudents():
    limitOption = int(input('How many records you wish to see?: '))

    sqlSelectAll = f"""
    SELECT * FROM Djangolessons
    LIMIT {limitOption};
    """
    mycursor.execute(sqlSelectAll)

    #fetchall() - отображение всех результатов
    result = mycursor.fetchall()

    #fetchone -  получение первого результата из sql скрипта
    # result2 = mycursor.fetchone()

    for num, student in enumerate(result,1):
        print(f'Student #{num}')
        print(f'Student name: {student[1]}'
              f'\nStudent age: {student[2]}'
              f'\nStudent country: {student[3]}')
        print('='*10)


def showStudentsByCountry(country, ageStudent):
    order = input('Which order you wish?: ')

    sqlSript = f"""
    SELECT * FROM Djangolessons
    WHERE country = '{country}' and age = {ageStudent}
    ORDER BY student_name {order};
    """

    mycursor.execute(sqlSript)
    result = mycursor.fetchall()

    print('Result: ')
    print('*'*20)
    for student in result:
        print(f'Student name: {student[1]}'
              f'\nStudent age: {student[2]}'
              f'\nStudent country: {student[3]}')
        print('=' * 10)

def main():
    menuText = """
        You are in the program.
        
        Please select an operation:
        1. Delete student
        2. Insert new student
        3. Update student
        4. Show all students data
        5. Show students by country
    """
    print(menuText)
    choiceMenu = int(input('Input menu option: '))

    if choiceMenu == 1:
        deleteStudent()
    elif choiceMenu == 2:
        insertStudent()
    elif choiceMenu == 3:
        updateStudent()
    elif choiceMenu == 4:
        showAllStudents()
    elif choiceMenu == 5:
        country = input('Please input country to find student: ')
        ageStudent = int(input('Enter age: '))
        showStudentsByCountry(country, ageStudent)


if __name__ == '__main__':
    main()

