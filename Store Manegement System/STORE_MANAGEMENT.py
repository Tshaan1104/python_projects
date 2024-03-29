
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector


db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost") 
 


db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
my_cursor=db.cursor()

query="CREATE TABLE IF NOT EXISTS products (date VARCHAR(10),prodName VARCHAR(20), prodPrice VARCHAR(50))" 
my_cursor.execute(query) 

db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
my_cursor=db.cursor()



query="CREATE TABLE IF NOT EXISTS sale (custName VARCHAR(20), date VARCHAR(10), prodName VARCHAR(30),qty INTEGER, price INTEGER )" 
my_cursor.execute(query)

res=[]
def prodtoTable():
    
    pname= prodName.get()
    price = prodPrice.get()
    dt = date.get()

    db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
    cursor = db.cursor()
    
   
    query = "INSERT INTO products(date,prodName,prodPrice) VALUES(%s,%s,%s)" 
    details = (dt,pname,price)

    
    try:
        cursor.execute(query,details)
        db.commit()
        messagebox.showinfo('Success',"Product added successfully")
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Error","Trouble adding data into Database")
    
    wn.destroy()

def addProd(): 
    global prodName, prodPrice, date, Canvas1,  wn
    

    wn = tkinter.Tk() 
    wn.title("Store Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add a Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lable1 = Label(labelFrame,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    
    lable2 = Label(labelFrame,text="Product Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.45, relheight=0.08)
        
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)
        
    
    lable3 = Label(labelFrame,text="Product Price : ", fg='black')
    lable3.place(relx=0.05,rely=0.6, relheight=0.08)
        
    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
           
    
    Btn = Button(wn,text="ADD",bg='#d1ccc0', fg='black',command=prodtoTable)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()


def removeProd():

    name = prodName.get()
    name = name.lower()
    

    db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
    cursor = db.cursor()
    

    query = "DELETE from products where LOWER(prodName) = '"+name+"'"
    try:
        cursor.execute(query)
        db.commit()


        messagebox.showinfo('Success',"Product Record Deleted Successfully")

    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Please check Product Name")
 
    wn.destroy()

def delProd(): 

    global prodName, Canvas1,  wn

    wn = tkinter.Tk() 
    wn.title("Store Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg="misty rose",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        

    lable = Label(labelFrame,text="Product Name : ", fg='black')
    lable.place(relx=0.05,rely=0.5)
        
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.5, relwidth=0.62)
    

    Btn = Button(wn,text="DELETE",bg='#d1ccc0', fg='black',command=removeProd)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()


def viewProds():
    global  wn
    wn = tkinter.Tk() 
    wn.title("Store Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn) 
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(wn,bg='old lace',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Products", fg='black', font = ('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25


    db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
    cursor=db.cursor()
    query = 'SELECT * FROM products'
    
    Label(labelFrame, text="%-50s%-50s%-50s"%('Date','Product','Price'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",fg='black').place (relx=0.05,rely=0.2)

    try:
        cursor.execute(query)
        res = cursor.fetchall() 
        
        for i in res:
            Label(labelFrame,text="%-50s%-50s%-50s"%(i[0],i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
            y += 0.1
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Failed to fetch files from database")
    
    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()


def bill():

    wn = tkinter.Tk() 
    wn.title("Store Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    headingFrame1 = Frame(wn,bg="lavender blush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Bill", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.35
    Label(labelFrame, text="%-40s%-40s%-40s%-40s"%('Product','Price','Quantity','Total'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.2)
    

    dt=date.get()
    cName=custName.get()
    totalBill=0
    
    db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
    cursor=db.cursor()
    query = 'SELECT * FROM products'
    
    
    if(len(name1.get()) != 0):

        i=res[0]
        qty=int(name1.get())
        total=qty*int(i[2])
        Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
        
 
    if(len(name2.get()) != 0):
        i=res[1]
        qty=int(name2.get())
        total=qty*int(i[2])
        Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
    

    if(len(name3.get()) != 0):
        i=res[2]
        qty=int(name3.get())
        total=qty*int(i[2])
        Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)

    Label(labelFrame, text = "------------------------------------------------------------------------------------",fg='black').place (relx=0.05,rely=y)
    y+=0.1
    Label(labelFrame,text="\t\t\t\t\t\t\t\t"+str(totalBill) ,fg='black').place(relx=0.07,rely=y)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
  
def newCust():    
    global wn,name1,name2,name3,date,custName
    wn = tkinter.Tk() 
    wn.title("Store Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    headingFrame1 = Frame(wn,bg="lavender blush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="New Customer", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    lable1 = Label(wn,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, )
        
    date = Entry(wn)
    date.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    lable2 = Label(wn,text="Customer Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.4, )
      

    custName = Entry(wn)
    custName.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.4)
    
    y = 0.3
    Label(labelFrame, text="Please enter the quantity of the products you want to buy",font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.1)
    
    Label(labelFrame, text="%-50s%-50s%-30s"%('Product','Price','Quantity'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.2)
    

    db=mysql.connector.connect(user="root",passwd="Shaan@11",host="localhost",database='Shop') 
    cursor=db.cursor()
    query = 'SELECT * FROM products'

    cursor.execute(query)
    res = cursor.fetchall() 
    print(res)
    c=1
    

    i=res[0]
    Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name1 = Entry(labelFrame)
    name1.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
    i=res[1]
    Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name2 = Entry(labelFrame)
    name2.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
    i=res[2]
    Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name3 = Entry(labelFrame)
    name3.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    

    Btn= Button(wn,text="Generate Bill",bg='#d1ccc0', fg='black',command=bill)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)

    wn.mainloop()

wn = tkinter.Tk() 
wn.title("Store Shop Management System")
wn.configure(bg='honeydew2')
wn.minsize(width=500,height=500)
wn.geometry("700x600")

headingFrame1 = Frame(wn,bg="snow3",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Store Management System", fg='green', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(wn,text="Add a Product",bg='LightBlue1', fg='black', width=20,height=2, command=addProd)
btn1['font'] = font.Font( size=12)
btn1.place(x=270,y=175)


btn2 = Button(wn,text="Delete a Product",bg='misty rose', fg='black',width=20,height=2,command=delProd)
btn2['font'] = font.Font( size=12)
btn2.place(x=270,y=255)

btn3 = Button(wn,text="View Products",bg='old lace', fg='black',width=20,height=2,command=viewProds)
btn3['font'] = font.Font( size=12)
btn3.place(x=270,y=335)

btn4 = Button(wn,text="New Customer",bg='lavender blush2', fg='black', width=20,height=2,command = newCust)
btn4['font'] = font.Font( size=12)
btn4.place(x=270,y=415)


wn.mainloop() 
