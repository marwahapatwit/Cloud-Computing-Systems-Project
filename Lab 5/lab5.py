import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password_here",
        database="my_guitar_shop"
    )

def query1_products_by_price_desc():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT product_code, product_name, list_price, discount_percent FROM Products ORDER BY list_price DESC")
    results = cursor.fetchall()
    conn.close()
    return results

def query2_customers_full_name():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, CONCAT(last_name, ', ', first_name) AS full_name FROM Customers WHERE last_name >= 'M' ORDER BY last_name ASC")
    results = cursor.fetchall()
    conn.close()
    return results

def query3_products_in_price_range():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT product_name, list_price, date_added FROM Products WHERE list_price > 500 AND list_price < 2000 ORDER BY date_added DESC")
    results = cursor.fetchall()
    conn.close()
    return results

def query4_order_items_with_totals():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT item_id, item_price, discount_amount, quantity,
               item_price * quantity AS price_total,
               discount_amount * quantity AS discount_total,
               (item_price - discount_amount) * quantity AS item_total
        FROM Order_Items
        WHERE (item_price - discount_amount) * quantity > 500
        ORDER BY item_total DESC
    """)
    results = cursor.fetchall()
    conn.close()
    return results

def query5_join_categories_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.category_name, p.product_name, p.list_price
        FROM Categories c
        JOIN Products p ON c.category_id = p.category_id
        ORDER BY c.category_name ASC, p.product_name ASC
    """)
    results = cursor.fetchall()
    conn.close()
    return results

def query6_customer_address_by_email():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
        FROM Customers c
        JOIN Addresses a ON c.customer_id = a.customer_id
        WHERE c.email = 'allan.sherwood@yahoo.com'
        ORDER BY a.zip_code ASC
    """)
    results = cursor.fetchall()
    conn.close()
    return results

def query7_shipping_addresses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
        FROM Customers c
        JOIN Addresses a ON c.customer_id = a.customer_id
        WHERE a.address_type = 1
        ORDER BY a.zip_code ASC
    """)
    results = cursor.fetchall()
    conn.close()
    return results
