import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pass123',
            database='employee'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None

def add_employee_to_db(name, age, phone, role, gender, salary, address):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (name, age, phone, role, gender, salary, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name, age, phone, role, gender, salary, address)
            )
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def update_employee_in_db(employee_id, name, age, phone, role, gender, salary, address):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE employees SET name=%s, age=%s, phone=%s, role=%s, gender=%s, salary=%s, address=%s WHERE id=%s",
                (name, age, phone, role, gender, salary, address, employee_id)
            )
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def fetch_all_employees():
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            conn.close()
            return rows
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []

def delete_employee_from_db(employee_id):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
