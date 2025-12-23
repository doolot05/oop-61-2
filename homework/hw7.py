import sqlite3


conn = sqlite3.connect("products.db")
cursor = conn.cursor()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)
    conn.commit()



def add_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()


def get_all_products():
    cursor.execute("SELECT rowid, * FROM products")
    return cursor.fetchall()



def get_by_rowid(row_id):
    cursor.execute("SELECT rowid, * FROM products WHERE rowid = ?", (row_id,))
    return cursor.fetchone()


def update_product(row_id, name, price, quantity):
    cursor.execute(
        "UPDATE products SET name = ?, price = ?, quantity = ? WHERE rowid = ?",
        (name, price, quantity, row_id)
    )
    conn.commit()


def delete_product(row_id):
    cursor.execute("DELETE FROM products WHERE rowid = ?", (row_id,))
    conn.commit()


if __name__ == "__main__":
    create_table()

    add_product("Apple", 50, 10)
    add_product("Banana", 30, 20)

    print("Все товары:")
    print(get_all_products())

    print("\nТовар с rowid = 1:")
    print(get_by_rowid(1))

    update_product(1, "Green Apple", 55, 15)

    print("\nПосле обновления:")
    print(get_all_products())

    delete_product(2)

    print("\nПосле удаления:")
    print(get_all_products())

    conn.close()
