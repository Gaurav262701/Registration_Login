
from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #-----------BG IMAGE-------------

        self.bg=ImageTk.PhotoImage(file="images/bg4.jpg")
        bg=Label(self.root,image=self.bg).place(x=150,y=0,relwidth=1,relheight=1)

        #----------Left Image---------------------
        self.left = ImageTk.PhotoImage(file="images/bg22.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=400)

        #-------Register Frame-----------------
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=400)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

#=====================================================================================

        name = Label(frame1, text="FULL NAME", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=70)
        self.txt_name= Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_name.place(x=50,y=100,width=200,)

        email = Label(frame1, text="EMAIL", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=350,y=70)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=350, y=100, width=200, )

#================================================================================

        phone = Label(frame1, text="CONTACT NO", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50,y=150)
        self.txt_phone = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_phone.place(x=50, y=180, width=200, )

        dob = Label(frame1, text="DATE OF BIRTH", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=350,y=150)
        self.txt_dob = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_dob.place(x=350, y=180, width=200, )

#==================================================================================


        psswrd = Label(frame1, text="PASSWORD", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50,y=220)
        self.txt_psswrd = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_psswrd.place(x=50, y=260, width=200, )

        Cpsswrd = Label(frame1, text="CONFIRM PASSWORD", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=350,y=220)
        self.txt_Cpsswrd = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_Cpsswrd.place(x=350, y=260, width=200, )

#========================================================================
        self.var_CHK=IntVar()
        CHK= Checkbutton(frame1,text="I Agree the Terms & Conditions",variable=self.var_CHK,onvalue=1,offvalue=0,bg = "white").place(x=50,y=290)
        self.btn_img=ImageTk.PhotoImage(file="images/th1.jpeg")
        btn= Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=50,y=320)
        btn_login = Button(self.root, text="SignIn",font=("times new roman",20), bd=0, cursor="hand2").place(x=220, y=350,width=150)

#========================================================================
    def register_data(self):
        if self.txt_name.get()=="" or self.txt_name.get()=="" or self.txt_email.get()=="" or self.txt_phone.get()=="" or self.txt_dob.get()=="" or self.txt_psswrd.get()=="" or self.txt_Cpsswrd.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        elif  self.txt_psswrd.get() != self.txt_Cpsswrd.get():
            messagebox.showerror("Error", "Incorrect Password", parent=self.root)

        elif self.var_CHK.get()==0:
            messagebox.showerror("Error", "Please Agree our Terms & Conditions", parent=self.root)

        else:
            messagebox.showinfo("Success", "Register Successful", parent=self.root)



root = Tk()
obj= Register(root)
root.mainloop()
