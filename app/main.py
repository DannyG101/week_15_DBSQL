from fastapi import FastAPI
from db_init import init_database
import dal

app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    response = dal.get_customers_by_credit_limit_range()
    return {"response": response}

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    response = dal.get_orders_with_null_comments()
    return {"response": response}
@app.get("/q3/customers-first-5")
def customers_first_5():
    response = dal.get_first_5_customers()
    return {"response": response}

@app.get("/q4/payments-total-average")
def payments_total_average():
    response = dal.get_payments_total_and_average()
    return {"response": response}

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    response = dal.get_employees_with_office_phone()
    return {"response": response}
@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    response = dal.get_customers_with_shipping_dates()
    return {"response": response}

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    response = dal.get_customer_quantity_per_order()
    return {"response": response}

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern(pattern: str = "son"):
    response = dal.get_customers_payments_by_lastname_pattern()
    return {"response": response}
