-- Query 1: Products by list price descending
SELECT product_code, product_name, list_price, discount_percent
FROM Products
ORDER BY list_price DESC;

-- Query 2: Customer full names with last names M–Z
SELECT first_name, last_name,
       CONCAT(last_name, ', ', first_name) AS full_name
FROM Customers
WHERE last_name >= 'M'
ORDER BY last_name ASC;

-- Query 3: Products between $500 and $2000
SELECT product_name, list_price, date_added
FROM Products
WHERE list_price > 500 AND list_price < 2000
ORDER BY date_added DESC;

-- Query 4: Order items with totals
SELECT item_id, item_price, discount_amount, quantity,
       item_price * quantity AS price_total,
       discount_amount * quantity AS discount_total,
       (item_price - discount_amount) * quantity AS item_total
FROM Order_Items
WHERE (item_price - discount_amount) * quantity > 500
ORDER BY item_total DESC;

-- Query 5: Join Categories and Products
SELECT c.category_name, p.product_name, p.list_price
FROM Categories c
JOIN Products p ON c.category_id = p.category_id
ORDER BY c.category_name ASC, p.product_name ASC;

-- Query 6: Customer addresses by email
SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
FROM Customers c
JOIN Addresses a ON c.customer_id = a.customer_id
WHERE c.email = 'allan.sherwood@yahoo.com'
ORDER BY a.zip_code ASC;

-- Query 7: Shipping addresses only
SELECT c.first_name, c.last_name, a.line1, a.city, a.state, a.zip_code
FROM Customers c
JOIN Addresses a ON c.customer_id = a.customer_id
WHERE a.address_type = 1
ORDER BY a.zip_code ASC;
