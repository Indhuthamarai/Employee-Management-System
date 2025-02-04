import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def open_payroll_page():
    subprocess.run(["python", "C:\\Users\\Thamarai selvan\\pyproj1\\payroll.py"])

def open_employee_records():
    subprocess.run(["python", "C:\\Users\\Thamarai selvan\\pyproj1\\employ.py"])

def resize_image(event):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    bg_image = Image.open("em.jpg")
    bg_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    root.bg_photo = bg_photo

root = tk.Tk()
root.title("Main Page")
root.geometry("600x600")

# Load and set the image as background
bg_image = Image.open("em.jpg")
bg_image = bg_image.resize((600, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas widget to display the background image
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(fill="both", expand=True)

# Add the background image to the Canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Keep a reference to the image
root.bg_photo = bg_photo

# Bind the resize_image function to the <Configure> event
root.bind("<Configure>", resize_image)

# Overlay frame for content to maintain readability
content_frame = tk.Frame(root, bg='white', bd=5)
content_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3, anchor='nw')

# Text "Employee Management System" below the image
title_label = tk.Label(content_frame, text="Employee Management System", bg='#3498db', fg='white', font=('Arial', 18, 'bold'))
title_label.pack(pady=10)

# Buttons to navigate to different pages
employee_records_button = tk.Button(content_frame, text="Employee Records", command=open_employee_records, bg='#f1c40f', fg='white', font=('Arial', 12), padx=10, pady=5)
employee_records_button.pack(pady=10)

payroll_button = tk.Button(content_frame, text="Payroll Page", command=open_payroll_page, bg='#e74c3c', fg='white', font=('Arial', 12), padx=10, pady=5)
payroll_button.pack(pady=10)

root.mainloop()
