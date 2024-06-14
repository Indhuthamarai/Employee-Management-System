from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import credentials as cr
from signup_page import SignUp

class LoginPage:
    def __init__(self, root):
        self.window = root
        self.window.title("Log In PySeek")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="white")

        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=0, y=0, width=450, relheight=1)

        label1 = Label(self.frame1, text="Py", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=100, y=300)
        label2 = Label(self.frame1, text="Seek", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=162, y=300)
        label3 = Label(self.frame1, text="It's all about Python", font=("times new roman", 13, "bold"), bg="yellow", fg="brown4").place(x=100, y=360)

        self.frame2 = Frame(self.window, bg="gray95")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=450)

        self.email_label = Label(self.frame3, text="Email Address", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50, y=40)
        self.email_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3, text="Password", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50, y=120)
        self.password_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show="*")
        self.password_entry.place(x=50, y=160, width=300)

        self.login_button = Button(self.frame3, text="Log In", command=self.login_func, font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="blue", fg="white").place(x=50, y=200, width=300)
        self.forgotten_pass = Button(self.frame3, text="Forgotten password?", command=self.forgot_func, font=("times new roman", 10, "bold"), bd=0, cursor="hand2", bg="white", fg="blue").place(x=125, y=260, width=150)
        self.create_button = Button(self.frame3, text="Create New Account", command=self.open_signup_window, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=80, y=320, width=250)

    def login_func(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and password=%s", (self.email_entry.get(), self.password_entry.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.window)
                else:
                    messagebox.showinfo("Success", "Welcome to the PySeek family", parent=self.window)
                    self.window.destroy()  # Close the login window
                    # Open the main application window (example implementation)
                    self.open_main_window()

                connection.close()

            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def open_main_window(self):
        # Implement the logic to open the main application window
        # Example: import and run main application
        import main  # Assuming there's a main.py in the same directory
        main.run()

    def forgot_func(self):
        if self.email_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your Email Id", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.email_entry.get())
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error!", "Email Id doesn't exist")
                else:
                    connection.close()
                    self.root = Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440+450+200")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root, text="Change your password", font=("times new roman", 20, "bold"), bg="white").place(x=10, y=10)
                    title4 = Label(self.root, text="It's quick and easy", font=("times new roman", 12), bg="white").place(x=10, y=45)
                    title5 = Label(self.root, text="Select your question", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=85)

                    self.sec_ques = ttk.Combobox(self.root, font=("times new roman", 13), state='readonly', justify=CENTER)
                    self.sec_ques['values'] = ("Select", "What's your pet name?", "Your first teacher name", "Your birthplace", "Your favorite movie")
                    self.sec_ques.place(x=10, y=120, width=270)
                    self.sec_ques.current(0)

                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=160)
                    self.ans = Entry(self.root, font=("arial"))
                    self.ans.place(x=10, y=195, width=270)
                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=235)
                    self.new_pass = Entry(self.root, font=("arial"))
                    self.new_pass.place(x=10, y=270, width=270)
                    self.create_button = Button(self.root, text="Submit", command=self.change_pass, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=95, y=340, width=200)

            except Exception as e:
                messagebox.showerror("Error", f"{e}")

    def open_signup_window(self):
        # Open the signup window
        self.window.destroy()
        root = Tk()
        obj = SignUp(root, self.open_main_window)  # Pass the open_main_window callback
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = LoginPage(root)
    root.mainloop()
