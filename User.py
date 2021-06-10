import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import webbrowser as wb

class User:
    def __init__(self):

        self.con = mysql.connector.connect(host="localhost", user="root", password="yourpassword", database="yourdatabase")
        self.cur = self.con.cursor()

    def tkin2(self):

        self.root2 = tk.Tk()
        self.mail = tk.StringVar()
        self.pwd = tk.StringVar()
        self.root2.title("User")
        self.root2.geometry('500x400')
        self.root2.iconbitmap('picturelocation.ico')
        bg = tk.PhotoImage(file="picturelocation.png")
        self.label1 = tk.Label(self.root2, image=bg)
        self.label1.place(x=0, y=0)
        self.userlab5 = ttk.Label(self.root2,text = "Email :", background="#61626B", font=("Times",14,"bold italic"), foreground="white").grid(row=3, column=0,pady=5)
        self.userentry5 = ttk.Entry(self.root2,textvariable = self.mail).grid(row=3,column=1,pady=5)
        self.userlab6 = ttk.Label(self.root2, text="Password :", background="#61626B", font=("Times",14,"bold italic"), foreground="white").grid(row=4, column=0,pady=5)
        self.userentry6 = ttk.Entry(self.root2, textvariable=self.pwd).grid(row=4, column=1,pady=5)
        self.button1 = tk.Button(self.root2,text = "login",command =self.login, bg="#742831").grid(row = 5, column = 1,pady=5)
        self.info = ttk.Label(self.root2, text="Are you a new user?",background="#61626B", font=("Times",12,"bold italic"), foreground="white").grid(row=7, column=0, pady=5, padx=2)
        self.button2 = tk.Button(self.root2,text="Sign in",command = self.UserRegister, bg="#742831").grid(row = 7,column = 1,pady=5)
        self.root2.mainloop()

    def UserRegister(self):

        mail1 = self.mail.get()
        pwds = self.pwd.get()
        insertUsers = "INSERT INTO user (email,password) VALUES (%s, %s)"
        values = (mail1,pwds)
        try:
            self.cur.execute(insertUsers,values)
            self.con.commit()
            messagebox.showinfo('Success', "You are Signup successfully")
            self.view()
        except:
            self.con.rollback()
            messagebox.showinfo("Error", "Can't add data into Database")
            self.con.close

    def login(self):
        mail1 = self.mail.get()
        pwds = self.pwd.get()
        if mail1=="" or pwds=="":
            messagebox.showinfo("please enter your mail id and password")
        else:
            self.cur.execute("select * from user where email = %s and password = %s",(mail1,pwds))
            row = self.cur.fetchone()
            if row == None:
                messagebox.showinfo("Your email id or password is invalid")
            else:
                self.view()

    def view(self):
        self.root2.destroy()

        #create tkinter window
        self.bkwin = tk.Tk()
        self.search = tk.StringVar()
        self.bkwin.geometry("800x500")
        self.bkwin.title("Books")
        self.bkwin.iconbitmap('picturelocation.ico')
        self.bkwin.config(bg="#D8BB71")

        #create database connectivity
        self.cur.execute("SELECT book_id,book_title,book_edition,Author FROM books")
        self.fetch_row = self.cur.fetchall()

        #table Heading
        self.lab1 = ttk.Label(self.bkwin,text="Book id",foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=0)
        self.lab2 = ttk.Label(self.bkwin, text="Book title",foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=1)
        self.lab3 = ttk.Label(self.bkwin, text="Edition",foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=2)
        self.lab4 = ttk.Label(self.bkwin, text="Author",foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=3)
        self.ent1 = ttk.Entry(self.bkwin, textvariable=self.search).grid(row=0, column=7)
        self.bt2 = tk.Button(self.bkwin, text="Search",fg="white", bg="maroon", relief="groove",
                             command=self.Search).grid(row=0, column=8)
        #display
        i = 1
        for bks in self.fetch_row:
            for j in range(len(bks)):
                self.bken = ttk.Label(self.bkwin, text=bks[j], borderwidth=10, relief='flat', anchor='w',
                                      padding=5, background="#D8BB71", font=("Times",14,"bold italic")).grid(row=i, column=j)
            self.bt = tk.Button(self.bkwin, text="View", fg="white", bg="green", relief="ridge",
                                command=lambda row=i, column=j: self.read(row, column)).grid(row=i,column=j + 1)
            i = i + 1

    def Search(self):
        self.bkwin1 = tk.Tk()
        self.bkwin1.geometry("800x500")
        self.bkwin1.title("Books")
        self.bkwin1.iconbitmap('picturelocation.ico')
        self.bkwin1.config(bg="#D8BB71")
        data = self.search.get()
        data = self.search.get()
        self.cur.execute("select book_id,book_title,book_edition,Author from books where book_title ='" + data + "'")
        self.fetch_row = self.cur.fetchall()
        if self.fetch_row == None:
            messagebox.showinfo("The book is currently not present in the database")
        else:
            self.lab1 = ttk.Label(self.bkwin1, text="Book id", foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=0)
            self.lab2 = ttk.Label(self.bkwin1, text="Book title", foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=1)
            self.lab3 = ttk.Label(self.bkwin1, text="Edition", foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=2)
            self.lab4 = ttk.Label(self.bkwin1, text="Author", foreground="red", background="#D8BB71", font=("Times",14,"bold italic")).grid(row=0, column=3)
        i = 1
        for bks in self.fetch_row:
            for j in range(len(bks)):
                self.bken = ttk.Label(self.bkwin1, text=bks[j], borderwidth=10, relief='flat', anchor='w',padding=5, background="#D8BB71", font=("Times",14,"bold italic")).grid(row=i, column=j)
            self.bt = tk.Button(self.bkwin1, text="View", fg="white", bg="green", relief="ridge", command=lambda row=i, column=j: self.read(row, column)).grid(row = i,column=j+1)
            i = i + 1


    def read(self,row,column):
        bk_info = self.fetch_row[row-1]
        id = bk_info[0]
        title = bk_info[1]
        ed = bk_info[2]
        blob_query = "select path from books where book_id = %s or book_title = %s and book_edition= %s"
        values = (id,title,ed)
        self.cur.execute(blob_query,values)
        fetched_row = self.cur.fetchall()
        data = str(fetched_row[0][0])
        filename = data
        wb.open_new(filename)

app1 = User()
app1.tkin2()

