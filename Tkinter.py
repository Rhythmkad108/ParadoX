import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.title('Illuminati')
#win.iconbitmap('C:/Users/hp/OneDrive/Desktop/illu.jpg')
name_var=tk.StringVar()
passw_var=tk.StringVar()
def check():
    global name
    global password
    name=name_var.get()
    password=passw_var.get()
    if (name=='ParadoX')&(password=='21103113'):
        return messagebox.showinfo("Tasks",'Prepare your soldiers!')
    elif (name=='Tejwir Kalia Wayne')&(password=='21103088'):
        return messagebox.showinfo("Tasks",'Arrange a meeting to talk about WW3.')
    elif (name=='Mishi Captures')&(password=='21103107'):
        return messagebox.showinfo("Tasks",'Prepare for Cyber Attack! Halt till notification.')
    elif (name=='Mani Bansal')&(password=='21103108'):
        return messagebox.showinfo("Tasks",'Manage the budget for our working.')
    else:
        return messagebox.showinfo("Unauthorised",'Request Denied.')
        
lbl1=tk.Label(win,text='Welcome to the official website of the PEC Illuminati',bg='Green',fg='White',font=("Times", "24", "bold italic"))
lbl1.place(x=0,y=0)
lbl2=tk.Label(win,text='Username',font=('16'),fg='Green')
lbl2.place(x=200,y=50)
entry1=tk.Entry(win,fg='Black',bd='4',textvariable=name_var)
entry1.place(x=300,y=50)
lbl3=tk.Label(win,text='Password',font=('16'),fg='Green')
lbl3.place(x=200,y=100)
entry2=tk.Entry(win,fg='Black',bd='4',show='*',textvariable = passw_var)
entry2.place(x=300,y=100)
button1=tk.Button(win,text='Sign in',activebackground='Green',activeforeground='White',fg='Green',command=check)
button1.place(x=300,y=150)
win.minsize(710,300)
win.mainloop
