from fastapi import FastAPI
from pydantic import BaseModel
from db import get_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Order(BaseModel):
    id: int
    item: str
    price: float
    status: str


# ✅ GET API (Fetch from DB)
@app.get("/orders")
def get_orders():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()

    orders = []
    for row in rows:
        orders.append({
            "id": row[0],
            "item": row[1],
            "price": float(row[2]),
            "status": row[3]
        })

    cur.close()
    conn.close()

    return orders


# ✅ POST API (Insert into DB)
@app.post("/orders")
def create_order(order: Order):

    if order.price <= 0:
        return {"error": "Invalid price"}

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO orders (id, item, price, status) VALUES (%s, %s, %s, %s);",
        (order.id, order.item, order.price, order.status)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Order stored in DB"}