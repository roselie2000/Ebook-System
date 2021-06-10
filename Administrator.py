
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector

class Administrator:
    def __init__(self):
        self.__Username = "any username"
        self.__Password = "any password"
        self.con = mysql.connector.connect(host="localhost", port=3306, user="root", password="yourpassword", database="yourdatabase")
        self.cur = self.con.cursor()

    def tkin1(self):
        self.root = tk.Tk()
        self.user = tk.StringVar()
        self.pwd = tk.StringVar()
        self.root.title("Administrator")
        self.root.geometry('500x300')
        self.root.iconbitmap('picturelocation.ico')
        bg = tk.PhotoImage(file="picturelocation.png")
        self.label1 = tk.Label(self.root, image=bg)
        self.label1.place(x=0, y=0)

        self.lab1 = ttk.Label(self.root, text="Username : ", background="#61626B", font=("Times",14,"bold italic"), foreground="white").grid(row = 0,column = 0, pady=5, padx=5)
        self.entry1 = ttk.Entry(self.root, textvariable=self.user).grid(row = 0, column = 1)
        self.lab2 = ttk.Label(self.root, text="Password : ",background="#61626B", font=("Times",14,"bold italic"), foreground="white").grid(row=2, column=0, pady=5, padx=5)
        self.entry2 = ttk.Entry(self.root, textvariable=self.pwd).grid(row=2, column=1)
        self.button = tk.Button(self.root,text = "login",command = self.login, bg="#742831", fg="white").grid(row = 4, column = 1, pady=5, padx=5)
        self.root.mainloop()

    def get_user(self):
        return self.__Username

    def get_password(self):
        return  self.__Password

    def login(self):
        self.user1 = self.get_user()
        self.pwd1 = self.get_password()
        self.users = self.user.get()
        self.pwds = self.pwd.get()
        if self.user1 == self.users and self.pwd1 == self.pwds:
            self.root.destroy()
            self.update()
        else:
            messagebox.showwarning("your user or password is invalid")

    def update(self):
        self.root1 = tk.Tk()
        self.id = tk.StringVar()
        self.title = tk.StringVar()
        self.edition = tk.StringVar()
        self.author = tk.StringVar()
        self.book = tk.StringVar()
        self.root1.title("Book Updation")
        self.root1.geometry("500x500")
        self.root1.iconbitmap('picturelocation.ico')
        bg = tk.PhotoImage(file="picturelocation.png")
        self.label1 = tk.Label(self.root1, image=bg)
        self.label1.place(x=0, y=0)

        # Book ID
        self.bklab1 = ttk.Label(self.root1, text="Book I'd : ", background="#A5A39E", font=("Times",12,"bold italic")).grid(row=1, column=0, padx=5, pady=5)
        self.bkentry1 = ttk.Entry(self.root1, textvariable=self.id).grid(row=1, column=1)

        # Title
        self.bklab2 = ttk.Label(self.root1, text="Book Title : ", background="#A5A39E", font=("Times",12,"bold italic")).grid(row=2, column=0, padx=5, pady=5)
        self.bkentry2 = ttk.Entry(self.root1, textvariable=self.title).grid(row=2, column=1)

        #Book Edition
        self.bklab = ttk.Label(self.root1, text = "Book version :", background="#A5A39E", font=("Times",12,"bold italic")).grid(row=3, column = 0, padx=5, pady=5)
        self.bkentry = ttk.Entry(self.root1,textvariable=self.edition).grid(row=3, column=1)

        # Book Author
        self.bklab3 = ttk.Label(self.root1, text="Author name : ", background="#A5A39E", font=("Times",12,"bold italic")).grid(row=4, column=0, padx=5, pady=5)
        self.bkentry3 = ttk.Entry(self.root1, textvariable=self.author).grid(row=4, column=1)

        # Book Browse
        self.bklab4 = ttk.Label(self.root1, text="Book : ", background="#A5A39E", font=("Times",12,"bold italic")).grid(row=5, column=0, padx=5, pady=5)

        # Browse button
        self.browsebutton = tk.Button(self.root1, text="Browse", command=self.browsefunc, bg="#7E7A8B").grid(row=5, column=1, padx=5, pady=5)

        # Submit Button
        self.SubmitBtn = tk.Button(self.root1, text="Submit", command=self.bookRegister, bg="#7E7A8B").grid(row=6, column=0, pady=5)
        self.deletebtn = tk.Button(self.root1, text="Delete", command=self.Delete, bg="#7E7A8B").grid(row=6, column=1, pady=5)
        self.quitBtn = tk.Button(self.root1, text="Quit", command=self.root1.destroy, bg="#7E7A8B").grid(row=7, column=0, pady=5)
        self.viewbtn = tk.Button(self.root1,text="View", command=self.view, bg="#7E7A8B").grid(row=6, column=2,pady=5)
        self.root1.mainloop()

    #browse function
    def browsefunc(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "select a file", filetype = (("pdf","*.pdf"), ("all Files","*.*")))
        self.label = ttk.Label(self.root1,text = self.filename).grid(row = 5, column = 2)
        with open(self.filename, 'rb') as file:
            self.data = file.read()


    def bookRegister(self):

        # self.con = mysql.connector.connect(host="localhost", port = 3306, user="root", password="Roselie@2000", database="Ebooks")
        # self.cur = con.cursor()
        bid = self.id.get()
        title = self.title.get()
        ed = self.edition.get()
        author = self.author.get()
        book_file = str(self.filename)
        insertBooks = "INSERT INTO books (book_id,book_title,book_edition,Author,path,book) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (bid,title,ed,author,self.filename,book_file)
        try:
            self.cur.execute(insertBooks,values)
            self.con.commit()
            messagebox.showinfo('Success', "Book added successfully")
        except:
            messagebox.showinfo("Error", "Can't add data into Database")

    def view(self):

        #create tkinter window
        self.bkwin = tk.Tk()
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
        self.lab4 = ttk.Label(self.bkwin, text="Author",foreground="red", background="#D8BB71", font=("Times",12,"bold italic")).grid(row=0, column=3)

        #display
        i = 1
        for bks in self.fetch_row:
            for j in range(len(bks)):
                self.bken = ttk.Label(self.bkwin, text=bks[j], borderwidth=10, relief='flat', anchor='w',
                                      padding=5, background="#D8BB71", font=("Times",12)).grid(row=i, column=j)
            i = i + 1

    def Delete(self):

        bid = self.id.get()
        try:
            self.cur.execute("delete from books where book_id ='" + bid + "'")
            self.con.commit()
            messagebox.showinfo('Success', "Book deleted successfully")
        except:
            messagebox.showinfo("Error", "Can't delete data into Database")

app = Administrator()
app.tkin1()






