import mysql.connector as mcon
from connectionInfo import infoconnection
from datetime import *

mysqldb_info = infoconnection()
mycursor = mysqldb_info.cursor()

def createView(viewName):
    sqlCreateView = f"""
        CREATE VIEW {viewName}
        AS SELECT customer_id, salesman_id, ord_date, purch_amount as 'Max order' 
        FROM Orders_prod
        WHERE purch_amount = (
        SELECT MAX(purch_amount) FROM Orders_prod
        );
    """

    mycursor.execute(sqlCreateView)
    print('View created!')

def showInfoFromView(viewName):
    showDataSql = f"""
    SELECT * FROM {viewName};
    """

    mycursor.execute(showDataSql)
    result = mycursor.fetchall()
    for i in result:
        print(f'Salesman id: {i[0]}')
        print(f'Customer id: {i[1]}')
        print(f'Max order: {i[3]}')

def showFromJoin():
    sqlScript = f"""
    SELECT  op.ord_no, op.customer_id, op.salesman_id, op.purch_amount ,chw.cust_name, op.ord_date, chw.city 
    FROM Orders_prod as op
    INNER JOIN customerhw as chw using(customer_id)
    INNER JOIN salesmanhw as shw on shw.salesman_id = op.salesman_id;
    """

    mycursor.execute(sqlScript)

    result = mycursor.fetchall()
    for numb, i in enumerate(result,1):
        ord_no, customer_id, salesman_id, purch_amount,\
        cust_name,date_purch, city = i

        #purch_date = datetime.strptime(date_purch, "%d, %B, %Y")
        purch_date = date_purch.strftime("%d-th of %B %Y ")

        print(f'Order number: {numb}')
        print('-'*30)
        print(f'Order number:{ord_no}'
              f'\nCustomer id: {customer_id}'
              f'\nSalesman id: {salesman_id}'
              f'\nPurchase amount: {purch_amount}'
              f'\nCustomer name: {cust_name}'
              f'\nCity: {city}'
              f'\nPurhased date: {purch_date}')
        print('='*30)



def main():
    #viewName = input('Enter view name: ')

    #createView(viewName)
    #showInfoFromView(viewName)

    showFromJoin()


if __name__ == '__main__':
    main()
