from typing import List, Dict, Any

from db import get_db_connection


def get_customers_by_credit_limit_range():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT customerName, creditLimit FROM customers
                WHERE creditLimit < 10000 OR creditLimit > 100000""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_orders_with_null_comments():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT orderNumber, comments FROM orders
                WHERE comments IS NOT NULL
                ORDER BY orderDate""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_first_5_customers():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT customerName, contactLastName, contactFirstName FROM customers
                ORDER BY contactLastName
                LIMIT 5""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_payments_total_and_average():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT SUM(amount) AS total_payments, 
                AVG(amount) AS average_payments, 
                MIN(amount) AS minimum_payment, 
                MAX(amount) AS max_payment 
                FROM payments""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_employees_with_office_phone():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT employees.firstName, employees.lastName, offices.phone AS office_phone
                FROM employees
                INNER JOIN offices
                ON employees.officeCode = offices.officeCode""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_customers_with_shipping_dates():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT customers.customerName, orders.orderDate FROM customers
                LEFT JOIN orders
                ON customers.customerNumber = orders.customerNumber""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_customer_quantity_per_order():
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT customers.customerName, SUM(orderdetails.quantityOrdered)
                FROM customers
                INNER JOIN orders
                ON customers.customerNumber = orders.customerNumber
                INNER JOIN orderdetails
                ON orders.orderNumber = orderdetails.orderNumber
                GROUP BY orders.orderNumber
                ORDER BY customers.customerName""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute("""SELECT customers.customerName, CONCAT(employees.firstName, ' ', employees.lastName) AS salesrep_name, SUM(payments.amount) AS total_payments
                FROM customers
                INNER JOIN employees
                ON customers.salesRepEmployeeNumber = employees.employeeNumber
                INNER JOIN payments
                ON customers.customerNumber = payments.customerNumber
                WHERE customers.contactFirstName LIKE '%ly%' OR customers.contactFirstName LIKE '%Mu%'
                GROUP BY payments.customerNumber
                ORDER BY total_payments DESC""")
    results = cur.fetchall()
    cur.close()
    connection.close()
    return results
