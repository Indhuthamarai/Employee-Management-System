import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from db_operations1 import add_payroll_record, fetch_all_payroll_records, delete_payroll_record, update_payroll_record

def add_record():
    name = entry_name.get()
    position = entry_position.get()
    hours_per_day = entry_hours_per_day.get()
    working_days = entry_working_days.get()

    if not name or not position or not hours_per_day or not working_days:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        total_hours = float(hours_per_day) * int(working_days)
        salary = calculate_salary(total_hours, position)
        add_payroll_record(name, total_hours, working_days, position, salary)  
        generate_receipt(name, total_hours, salary)  
        messagebox.showinfo("Success", f"Payroll record added successfully. Total Salary: ${salary:.2f}")
        fetch_data()
        clear_fields()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for hours and days.")

def calculate_salary(total_hours, position):
    if position == "Manager":
        rate_per_hour = 60
    elif position == "Developer":
        rate_per_hour = 45
    elif position == "Intern":
        rate_per_hour = 20
    else:
        rate_per_hour = 10  

    return total_hours * rate_per_hour * rate_per_hour

def generate_receipt(name, total_hours, salary):
    receipt = f"Name: {name}\nTotal Hours Worked: {total_hours}\nSalary: ${salary:.2f}"
    messagebox.showinfo("Salary Receipt", receipt)

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_position.delete(0, tk.END)
    entry_hours_per_day.delete(0, tk.END)
    entry_working_days.delete(0, tk.END)

def delete_record():
    selected = payroll_table.focus()
    if selected:
        selected_record = payroll_table.item(selected)['values']
        delete_payroll_record(selected_record[0])
        messagebox.showinfo("Success", "Payroll record deleted successfully.")
        fetch_data()

def update_record():
    selected = payroll_table.focus()
    if selected:
        selected_record = payroll_table.item(selected)['values']
        entry_name.delete(0, tk.END)
        entry_position.delete(0, tk.END)
        entry_hours_per_day.delete(0, tk.END)
        entry_working_days.delete(0, tk.END)

        entry_name.insert(0, selected_record[1])
        entry_position.insert(0, selected_record[4])
        hours_per_day = float(selected_record[2]) / int(selected_record[3])
        entry_hours_per_day.insert(0, hours_per_day)
        entry_working_days.insert(0, selected_record[3])

        update_button.config(text="Update", command=lambda: update_selected_record(selected_record[0]))
    else:
        messagebox.showwarning("Error", "Select a record to update.")

def update_selected_record(id):
    name = entry_name.get()
    position = entry_position.get()
    hours_per_day = entry_hours_per_day.get()
    working_days = entry_working_days.get()

    if not name or not position or not hours_per_day or not working_days:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        total_hours = float(hours_per_day) * int(working_days)
        salary = calculate_salary(total_hours, position)
        update_payroll_record(id, name, total_hours, working_days, position, salary)
        messagebox.showinfo("Success", "Payroll record updated successfully.")
        fetch_data()
        clear_fields()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for hours and days.")

def fetch_data():
    rows = fetch_all_payroll_records()
    payroll_table.delete(*payroll_table.get_children())
    for row in rows:
        payroll_table.insert('', 'end', values=row)

root = tk.Tk()
root.title("Payroll Management System")
root.geometry("800x600")
root.configure(bg='#2C3E50')

image = Image.open("img.jpg")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight() // 3), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=photo)
label_image.place(x=0, y=0, relwidth=1, relheight=0.2)

tk.Label(root, text="Payroll Management System", bg='#2C3E50', fg='white', font=('Arial', 20)).place(relx=0.5, rely=0.25, anchor='center')

style = ttk.Style()
style.configure('TButton', foreground='white', background='#3498DB', font=('Arial', 10, 'bold'))
style.configure('TEntry', foreground='#2C3E50', font=('Arial', 10))
style.configure('Treeview', foreground='#2C3E50', background='white', fieldbackground='white', font=('Arial', 10))

tk.Label(root, text="Name:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.35)
entry_name = tk.Entry(root, width=30)
entry_name.place(relx=0.25, rely=0.35)

tk.Label(root, text="Position:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.4)
entry_position = tk.Entry(root, width=30)
entry_position.place(relx=0.25, rely=0.4)

tk.Label(root, text="Hours Worked Per Day:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.45)
entry_hours_per_day = tk.Entry(root, width=30)
entry_hours_per_day.place(relx=0.25, rely=0.45)

tk.Label(root, text="Working Days:", bg='#2C3E50', fg='white').place(relx=0.05, rely=0.5)
entry_working_days = tk.Entry(root, width=30)
entry_working_days.place(relx=0.25, rely=0.5)

add_button = ttk.Button(root, text="Add Record", command=add_record, style='Green.TButton')
add_button.place(relx=0.05, rely=0.6)

update_button = ttk.Button(root, text="Update Record", command=update_record, style='Green.TButton')
update_button.place(relx=0.25, rely=0.6)

delete_button = ttk.Button(root, text="Delete Record", command=delete_record, style='Green.TButton')
delete_button.place(relx=0.45, rely=0.6)

clear_button = ttk.Button(root, text="Clear", command=clear_fields, style='Green.TButton')
clear_button.place(relx=0.65, rely=0.6)

style.configure('Green.TButton', foreground='green', background='green', font=('Arial', 10, 'bold'))

columns = ("ID", "Name", "Total Hours Worked", "Working Days", "Position", "Salary")
payroll_table = ttk.Treeview(root, columns=columns, show="headings", height=10)
payroll_table.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

for col in columns:
    payroll_table.heading(col, text=col.capitalize())
    payroll_table.column(col, width=100, minwidth=50)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=payroll_table.yview)
scrollbar.place(relx=0.95, rely=0.65, relheight=0.3)
payroll_table.configure(yscrollcommand=scrollbar.set)

fetch_data()
root.mainloop()