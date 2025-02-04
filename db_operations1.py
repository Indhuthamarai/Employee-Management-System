import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pass123',
            database='payroll'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None

def add_payroll_record(name, total_hours, working_days, position, salary):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO payroll_records (name, total_hours, working_days, position, salary) VALUES (%s, %s, %s, %s, %s)",
                (name, total_hours, working_days, position, salary)
            )
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def fetch_all_payroll_records():
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM payroll_records")
            rows = cursor.fetchall()
            conn.close()
            return rows
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []

def delete_payroll_record(payroll_id):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM payroll_records WHERE id=%s", (payroll_id,))
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
def update_payroll_record(payroll_id, name, total_hours, working_days, position, salary):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE payroll_records SET name=%s, total_hours=%s, working_days=%s, position=%s, salary=%s WHERE id=%s",
                (name, total_hours, working_days, position, salary, payroll_id)
            )
            conn.commit()
            conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def get_payroll_record(payroll_id):
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM payroll_records WHERE id=%s", (payroll_id,))
            row = cursor.fetchone()
            conn.close()
            return row
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None