import sqlite3
DB_NAME = "shop.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product TEXT,
        price REAL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    """)

    conn.commit()
    conn.close()

def add_customer(name, city,):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, city) VALUES (?, ?)",
        (name, city)
    )
    conn.commit()
    conn.close()
def add_order(customer_id, product, price, ):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_id, product, price) VALUES (?, ?, ?)",
        (customer_id, product, price)
    )
    conn.commit()
    conn.close()

def show_customers_with_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT customers.name, customers.city, orders.product, orders.price
        FROM customers
        LEFT JOIN orders ON customers.id = orders.customer_id
        """)
    rows = cursor.fetchall()
    print("\n Клиенты и их заказы:")
    for row in rows:
        print(f"Имя: {row[0]}, Город: {row[1]}, Товар: {row[2]}, Цена: {row[3]}")
    conn.close()

def aggregate_functions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders")
    print(" Количество заказов:", cursor.fetchone()[0])

    cursor.execute("SELECT MAX(price) FROM orders")
    print(" Максимальная цена:", cursor.fetchone()[0])

    cursor.execute("SELECT AVG(price) FROM orders")
    print(" Средняя цена:", cursor.fetchone()[0])

    conn.close()

def orders_count_by_customer():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customers.name, COUNT(orders.id)
        FROM customers
        LEFT JOIN orders ON customers.id = orders.customer_id
        GROUP BY customers.id
        """)

    rows = cursor.fetchall()

    print("\n Количество заказов у каждого клиента:")
    for row in rows:
        print(f"{row[0]} — {row[1]} заказ(ов)")

    conn.close()

def customers_with_expensive_orders(min_price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name FROM customers
    WHERE id IN (
        SELECT customer_id FROM orders WHERE price > ?
    )
    """, (min_price,))

    rows = cursor.fetchall()

    print(f"\n Клиенты с заказами дороже {min_price}:")
    for row in rows:
        print(row[0])
    conn.close()

def create_view():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE VIEW IF NOT EXISTS customer_orders_view AS
    SELECT customers.name, customers.city, orders.product, orders.price
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    """)

    conn.commit()
    conn.close()


def show_view_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer_orders_view")
    rows = cursor.fetchall()

    print("\n Данные из VIEW:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    create_tables()

    add_customer("Алиса", "Бишкек")
    add_customer("Боб", "Ош")

    add_order(1, "Ноутбук", 85000)
    add_order(1, "Мышь", 1500)
    add_order(2, "Телефон", 60000)

    show_customers_with_orders()
    aggregate_functions()
    orders_count_by_customer()
    customers_with_expensive_orders(50000)

    create_view()
    show_view_data()