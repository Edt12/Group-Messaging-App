import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import sqlite3
import  hashlib
import os
conn=sqlite3.connect("Teams+/Database.db")
cursor=conn.cursor()

#defining screen height and width
ScreenHeightStarting=800
ScreenWidthStarting=800
DirectoryPath=os.path.dirname(os.path.abspath(__file__))#gets directory path of the file




class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(str((ScreenWidthStarting))+"x"+str((ScreenHeightStarting)))
        self.title("Login")
        def Login():
            Username=UsernameEntry.get()
            Password=PasswordEntry.get()
            HashedUsername=hashlib.sha3_512(Username)
            HashedPassword=hashlib.sha3_512(Password)
            cursor.execute("Select*from UsernamesAndPasswords")
            UsersAndPasswords=cursor.fetchall()
            
       
        Button=ctk.CTkButton(self,
                             text="Enter",
                             hover_color="blue",
                             command=Login)
        
        Button.place(relheight=0.05,relwidth=0.1,relx=0.6,rely=0.4)
        UsernameEntry=ctk.CTkEntry(self,placeholder_text="Username")
        UsernameEntry.place(relheight=0.05,relwidth=0.15,relx=0.4,rely=0.4)
        PasswordEntry=ctk.CTkEntry(self,placeholder_text="Password")
        PasswordEntry.place(relheight=0.05,relwidth=0.15,relx=0.4,rely=0.5)
        Title=ctk.CTkLabel(self,text="Teams+",text_color="White",font=('Bold',20))
        Title.place(relheight=0.1,relwidth=0.2,relx=0.4,rely=0.3)
        

cursor.execute("""Create Table if not exists UsernamesAndPasswords
    (Username blob(512) Primary Key
    ,Password blob(512)
    )""")

Main=Login()
Main.mainloop()