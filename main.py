from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *

db=Database("SqliteDatabase.db")

fenetre=Tk()
fenetre.title("Govolunteer")
fenetre.geometry("1920x1080")
fenetre.configure(bg="black")

#titre
lb=Label(fenetre,text="GoVolunteer is a link between donaters and associations",font=("times",30,"bold"),fg="#BB9B21",bg="black")
lb.pack()

#sous-titre
lb=Label(fenetre,text="<< The best way to find yourself is to lose yourself in the service of others >>",font=("inherit",12),fg="white",bg="black")
lb.pack()

frame1=Frame(fenetre,padx=40,pady=0,bg="black")
frame1.pack(side=RIGHT,fill=BOTH)

#photo
photo=PhotoImage(file = 'donate.png')
label=Label(fenetre,image=photo,width=600,height=400,bg="black")
label.pack()

#titre
Title_Label=Label(frame1,text="GO VOLUNTEER",font=("arial",18,"bold"),fg="WHITE",bg="black",pady=20)
Title_Label.grid(columnspan=2)

# case nom
Name_Label=Label(frame1,text="Full Name",fg="white",bg="black",font=("arial",16,"bold"))
Name_Label.grid(row=1,column=0)
name=StringVar()
txtName=Entry(frame1,textvariable=name,font=("arial",16),width=38)
txtName.grid(row=1,column=1)


#case CIN
CIN_Label=Label(frame1,text="CIN",width=10,fg="white",bg="black",font=("arial",16,"bold"),pady=10)
CIN_Label.grid(row=2,column=0)
cin=StringVar()
txtCIN=Entry(frame1,textvariable=cin,font=("arial",16),width=38)
txtCIN.grid(row=2,column=1)

#case Telephone
Tel_Label=Label(frame1,text="Phone number",width=15,fg="white",bg="black",font=("arial",16,"bold"),pady=10)
Tel_Label.grid(row=3,column=0)
telephone=StringVar()
txtTel=Entry(frame1,font=("arial",16),width=38,textvariable=telephone)
txtTel.grid(row=3,column=1)

#case Address
Add_Label=Label(frame1,text="Address",width=10,fg="white",bg="black",font=("arial",16,"bold"),pady=10)
Add_Label.grid(row=4,column=0)
address=StringVar()
txtAdd=Entry(frame1,font=("arial",16),width=38,textvariable=address)
txtAdd.grid(row=4,column=1)

#case Type of donation
TypeDonation_Label=Label(frame1,text="Type of donation",width=18,fg="white",bg="black",font=("arial",16,"bold"),pady=10)
TypeDonation_Label.grid(row=5,column=0)
typedonation=StringVar()
cbDonat=ttk.Combobox(frame1,width=36,textvariable=typedonation,state="readonly",font=("arial",16))
cbDonat['values']=("Money","Food","Clothes","Furnitures","Medecines","Others")
cbDonat.grid(row=5,column=1)

#case Description of donation
Description_Label=Label(frame1,text="Description of donation",width=18,fg="white",bg="black",font=("arial",16,"bold"),pady=10)
Description_Label.grid(row=6,column=0)
description=StringVar()
txtDes=Entry(frame1,font=("arial",16),width=38,textvariable=description)
txtDes.grid(row=6,column=1)


#Bouttons
btn_frame=Frame(frame1,bg="#2d3436")
btn_frame.grid(row=7,column=1,columnspan=4)

def fetchData():
    table.delete(*table.get_children())
    count=0
    for row in db.fetch_record():
        count+=1
        table.insert("",END,values=(count,row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

def addData():
    if txtName.get()=="" or txtCIN.get()=="" or txtTel.get()=="" or txtAdd.get()=="" or cbDonat.get()==""  or txtDes.get()=="" :
        messagebox.showinfo("Message","Please Fill All Records")
    else:
        db.insert(txtName.get(),txtCIN.get(),txtTel.get(),txtAdd.get(),cbDonat.get(),txtDes.get())
        fetchData()
        clearData()
        messagebox.showinfo("Message","Record Insert Successfully")

def getrecord(event):
    srow = table.focus()
    data = table.item(srow)
    global row
    row = data['values']
    name.set(row[2])
    cin.set(row[3])
    telephone.set(row[4])
    typedonation.set(row[6])
    description.set(row[7])
    address.set(row[5])

def updateData():
    if txtName.get() == "" or txtCIN.get() == "" or txtTel.get() == "" or txtAdd.get() == "" or cbDonat.get() == "" or txtDes.get()=="":
        messagebox.showinfo("Message", "Please Fill All Records")
    else:
        db.update_record(txtName.get(), txtCIN.get(), txtTel.get(), txtAdd.get(), cbDonat.get(), txtDes.get(), (row[1]))
        fetchData()
        clearData()
        messagebox.showinfo("Message", "Record Update Successfully")

def deleteData():
    db.remove_record(row[1])
    fetchData()
    clearData()
    messagebox.showinfo("Message", "Record Delete Successfully")

def clearData():
    name.set("")
    cin.set("")
    telephone.set("")
    address.set("")
    typedonation.set("")
    description.set("")

btnSub=Button(btn_frame,text="Insert",bg="#AC781D",fg="black",width=5,padx=20,pady=5,font=("times",16,"bold"),command=addData)
btnSub.grid(row=0,column=0)

btnUp=Button(btn_frame,text="Update",bg="#967817",fg="black",width=5,padx=20,pady=5,font=("times",16,"bold"),command=updateData)
btnUp.grid(row=0,column=1)

btnDel=Button(btn_frame,text="Delete",bg="#976600",fg="black",width=5,padx=20,pady=5,font=("times",16,"bold"),command=deleteData)
btnDel.grid(row=0,column=2)

btnClr=Button(btn_frame,text="Clear",bg="#CC6600",fg="black",width=5,padx=20,pady=5,font=("times",16,"bold"),command=clearData)
btnClr.grid(row=0,column=3)

# cree-table

myFrame=Frame(fenetre)
myFrame.place(x=0,y=470,width=1300,height=500)

