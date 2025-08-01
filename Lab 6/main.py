from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory representation of products
products_db = {
    "GTR001": {"product_name": "Fender Stratocaster", "list_price": 1299.99, "discount_percent": 10.0},
    "BAS001": {"product_name": "Yamaha Bass", "list_price": 899.99, "discount_percent": 5.0},
}

class Product(BaseModel):
    product_name: str
    list_price: float
    discount_percent: float

@app.get("/products")
def list_products():
    return products_db

@app.get("/product")
def get_product(product_code: str = Query(...)):
    if product_code in products_db:
        return products_db[product_code]
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/product")
def update_product(product_code: str, product: Product):
    products_db[product_code] = product.dict()
    return {"message": "Product updated", "product": products_db[product_code]}

@app.get("/discounted-products")
def get_discounted_products(min_discount: float = 0.0):
    return {code: data for code, data in products_db.items() if data["discount_percent"] >= min_discount}

@app.get("/total-products")
def get_total_products():
    return {"total": len(products_db)}

@app.put("/add-product")
def add_product(product_code: str, product: Product):
    if product_code in products_db:
        raise HTTPException(status_code=400, detail="Product already exists")
    products_db[product_code] = product.dict()
    return {"message": "Product added"}

@app.put("/delete-product")
def delete_product(product_code: str):
    if product_code not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_db[product_code]
    return {"message": "Product deleted"}

@app.get("/product-names")
def get_product_names():
    return [data["product_name"] for data in products_db.values()]

@app.get("/average-price")
def get_average_price():
    if not products_db:
        return {"average_price": 0.0}
    total_price = sum(product["list_price"] for product in products_db.values())
    return {"average_price": total_price / len(products_db)}

@app.get("/product-exists")
def product_exists(product_code: str):
    return {"exists": product_code in products_db}