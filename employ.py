import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from db_operations import add_employee_to_db, fetch_all_employees, update_employee_in_db, delete_employee_from_db

def add_employee():
    name = entry_name.get()
    age = entry_age.get()
    phone = entry_phone.get()
    role = entry_role.get()
    gender = gender_var.get()
    salary = entry_salary.get()
    address = entry_address.get("1.0", "end-1c")

    if not name or not age or not phone or not role or not gender or not salary or not address:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    if not age.isdigit() or not salary.replace('.', '', 1).isdigit():
        messagebox.showwarning("Input Error", "Age and Salary must be numeric.")
        return

    add_employee_to_db(name, int(age), phone, role, gender, float(salary), address)
    messagebox.showinfo("Success", "Employee added successfully.")
    clear_entries()
    fetch_data()

def fetch_data():
    rows = fetch_all_employees()
    employee_table.delete(*employee_table.get_children())
    for row in rows:
        employee_table.insert('', 'end', values=row)

def get_selected_employee(event):
    global selected_employee
    selected = employee_table.focus()
    if selected:
        selected_employee = employee_table.item(selected)['values']
        entry_name.delete(0, tk.END)
        entry_name.insert(tk.END, selected_employee[1])
        entry_age.delete(0, tk.END)
        entry_age.insert(tk.END, selected_employee[2])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(tk.END, selected_employee[3])
        entry_role.delete(0, tk.END)
        entry_role.insert(tk.END, selected_employee[4])
        gender_var.set(selected_employee[5])
        entry_salary.delete(0, tk.END)
        entry_salary.insert(tk.END, selected_employee[6])
        entry_address.delete(1.0, tk.END)  # Corrected here
        entry_address.insert(tk.END, selected_employee[7])

def update_employee():
    if not selected_employee:
        messagebox.showwarning("Selection Error", "Please select an employee to update.")
        return

    name = entry_name.get()
    age = entry_age.get()
    phone = entry_phone.get()
    role = entry_role.get()
    gender = gender_var.get()
    salary = entry_salary.get()
    address = entry_address.get("1.0", "end-1c")

    if not name or not age or not phone or not role or not gender or not salary or not address:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    if not age.isdigit() or not salary.replace('.', '', 1).isdigit():
        messagebox.showwarning("Input Error", "Age and Salary must be numeric.")
        return

    update_employee_in_db(selected_employee[0], name, int(age), phone, role, gender, float(salary), address)
    messagebox.showinfo("Success", "Employee updated successfully.")
    clear_entries()
    fetch_data()

def delete_employee():
    if not selected_employee:
        messagebox.showwarning("Selection Error", "Please select an employee to delete.")
        return

    delete_employee_from_db(selected_employee[0])
    messagebox.showinfo("Success", "Employee deleted successfully.")
    clear_entries()
    fetch_data()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    gender_var.set("")
    entry_salary.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)

root = tk.Tk()
root.title("Employee Management System")
root.geometry("800x600")
root.configure(bg='#2C3E50')

# Load and display the image
image = Image.open("img.jpg")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight() // 3), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=photo)
label_image.place(x=0, y=0, relwidth=1, relheight=0.2)

# Text "Employee Management System" below the image
tk.Label(root, text="Employee Records System", bg='#2C3E50', fg='white', font=('Arial', 20)).place(relx=0.5, rely=0.25, anchor='center')

# Modify appearance of widgets
style = ttk.Style()
style.configure('TButton', foreground='white', background='#3498DB', font=('Arial', 10, 'bold'))
style.configure('TEntry', foreground='#2C3E50', font=('Arial', 10))
style.configure('Treeview', foreground='#2C3E50', background='white', fieldbackground='white', font=('Arial', 10))

# Input fields
tk.Label(root, text="Name:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.35)
entry_name = tk.Entry(root, width=30)
entry_name.place(relx=0.15, rely=0.35)

tk.Label(root, text="Age:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.4)
entry_age = tk.Entry(root, width=30)
entry_age.place(relx=0.15, rely=0.4)

tk.Label(root, text="Phone:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.45)
entry_phone = tk.Entry(root, width=30)
entry_phone.place(relx=0.15, rely=0.45)

tk.Label(root, text="Role:", bg='#2C3E50', fg='white').place(relx=0.45, rely=0.35)
entry_role = tk.Entry(root, width=30)
entry_role.place(relx=0.55, rely=0.35)

tk.Label(root, text="Gender:", bg='#2C3E50', fg='white').place(relx=0.45, rely=0.4)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], width=27)
gender_dropdown.place(relx=0.55, rely=0.4)

tk.Label(root, text="Salary:", bg='#2C3E50', fg='white').place(relx=0.45, rely=0.45)
entry_salary = tk.Entry(root, width=30)
entry_salary.place(relx=0.55, rely=0.45)

tk.Label(root, text="Address:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.5)
entry_address = tk.Text(root, width=30, height=2)
entry_address.place(relx=0.15, rely=0.5)

# Buttons
add_button = ttk.Button(root, text="Add Employee", command=add_employee, style='Green.TButton')
add_button.place(relx=0.05, rely=0.55)

update_button = ttk.Button(root, text="Update Employee", command=update_employee, style='Green.TButton')
update_button.place(relx=0.25, rely=0.55)

delete_button = ttk.Button(root, text="Delete Employee", command=delete_employee, style='Green.TButton')
delete_button.place(relx=0.45, rely=0.55)

clear_button = ttk.Button(root, text="Clear", command=clear_entries, style='Green.TButton')
clear_button.place(relx=0.65, rely=0.55)

style.configure('Green.TButton', foreground='green', background='green', font=('Arial', 10, 'bold'))

# Table
columns = ("id", "name", "age", "phone", "role", "gender", "salary", "address")
employee_table = ttk.Treeview(root, columns=columns, show="headings", height=10)
employee_table.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.35)

for col in columns:
    employee_table.heading(col, text=col.capitalize())
    employee_table.column(col, width=100, minwidth=50)

employee_table.bind('<<TreeviewSelect>>', get_selected_employee)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=employee_table.yview)
scrollbar.place(relx=0.95, rely=0.6, relheight=0.35)
employee_table.configure(yscrollcommand=scrollbar.set)

fetch_data()
root.mainloop()
