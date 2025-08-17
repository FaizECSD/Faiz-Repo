import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

class Main_Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('550x550')
        self.title('Bank Portal')
        
        L1=ctk.CTkLabel(self, text='Choose an Operation')
        B1=ctk.CTkButton(self, text='Open an Account',command=self.open_acc)
        B2=ctk.CTkButton(self, text='Delete an Account',command=self.del_acc)
        B3=ctk.CTkButton(self, text='Deposit Money',command=self.dep_acc)
        B4=ctk.CTkButton(self, text='Withdrawal',command=self.with_acc) 
        B5=ctk.CTkButton(self, text='Search an Account',command=self.srch_acc)
        B6=ctk.CTkButton(self, text='Exit',command=self.destroy)
        L1.pack(pady=20)
        B1.pack(pady=10)
        B2.pack(pady=10)
        B3.pack(pady=10)
        B4.pack(pady=10)
        B5.pack(pady=10)
        B6.pack(pady=10)
    def open_acc(self):
        self.withdraw()
        f1=Open_acc(self)
        f1.mainloop()
        
    def del_acc(self):
        self.withdraw()
        f2=Del_acc(self)
        f2.mainloop() 
        
    def dep_acc(self):
        self.withdraw()
        f3=Dep_acc(self)
        f3.mainloop()
        
    def with_acc(self):
        self.withdraw()
        f4=With_acc(self)
        f4.mainloop()
        
    def srch_acc(self):
        self.withdraw()
        f5=Srch_acc(self)
        f5.mainloop()
        
class Open_acc(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Open Account")
        self.geometry("550x550")

             
        self.acc_type=ctk.IntVar()
        L1 = ctk.CTkLabel(master=self, text="Enter Account Number")
        L1.pack(pady=5)
        self.E1 = ctk.CTkEntry(master=self)
        self.E1.pack(pady=5)

        L2 = ctk.CTkLabel(master=self, text="Enter Account Holder's Name")
        L2.pack(pady=5)
        self.E2 = ctk.CTkEntry(master=self)
        self.E2.pack(pady=5)

        L3 = ctk.CTkLabel(master=self, text="Choose Account's Type")
        L3.pack(pady=5)
        R1=ctk.CTkRadioButton(self, text='Savings',variable=self.acc_type,value=1)
        R2=ctk.CTkRadioButton(self, text='Current',variable=self.acc_type,value=2)
        R1.pack(pady=5)
        R2.pack(pady=5)  
        #self.E3 = ctk.CTkEntry(master=self)
        #self.E3.pack(pady=5)

        L4 = ctk.CTkLabel(master=self, text="Enter Initial Balance")
        L4.pack(pady=5)
        self.E4 = ctk.CTkEntry(master=self)
        self.E4.pack(pady=5)
        B1 = ctk.CTkButton(master=self, text="Open Account", command=self.create_account)
        B1.pack(pady=20)
        B2 = ctk.CTkButton(master=self, text="Back", command=self.back_to_main)
        B2.pack(pady=20)
        
    def create_account(self): 
        mydb = mysql.connector.connect(host='localhost', user='root', password='faiz', database='faizdata')
        crsr = mydb.cursor()
        try: 
           accno = self.E1.get() 
           name = self.E2.get()
           #acctype = self.E3.get()
           balance = self.E4.get()
           ch=self.acc_type.get()
           if ch==1:
               acctype='Savings'
           else:
               acctype='Current'
           sql = "INSERT INTO accounts VALUES ("+accno+",'"+name+"','"+acctype+"',"+balance+")" 
           crsr.execute(sql) 
           mydb.commit() 
           messagebox.showinfo("Success", "Account Created Successfully!") 
      
        except Exception as e: 
           messagebox.showerror("Error", f"Failed to create account: {e}") 
           mydb.rollback() 
           
        mydb.close()
        crsr.close()
       
        
    def back_to_main(self):
        self.destroy()
        self.master.deiconify()
       
            
class Del_acc(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Delete Account")
        self.geometry("250x350")

             

        L1 = ctk.CTkLabel(master=self, text="Enter Account Number")
        L1.pack(pady=5)
        self.E1 = ctk.CTkEntry(master=self)
        self.E1.pack(pady=5)
        B1 = ctk.CTkButton(master=self, text="Delete Account", command=self.delete_acc)
        B1.pack(pady=20)
        B2 = ctk.CTkButton(master=self, text="Back", command=self.back_to_main)
        B2.pack(pady=20)

    def delete_acc(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='faiz', database='faizdata')
        crsr = mydb.cursor()
        try: 
           accno = self.E1.get() 
           sql="delete from accounts where Account_Number="+accno
           crsr.execute(sql)
           mydb.commit()
           messagebox.showinfo('Account Deletion',"Account Terminated Successfully!!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete account: {e}") 
            mydb.rollback() 
        mydb.close()
        crsr.close()

       
    def back_to_main(self):
        self.destroy()
        self.master.deiconify()
        
    
class Dep_acc(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Deposit Money")
        self.geometry("250x350")

             

        L1 = ctk.CTkLabel(master=self, text="Enter Account Number")
        L1.pack(pady=5)
        self.E1 = ctk.CTkEntry(master=self)
        self.E1.pack(pady=5)

        L2 = ctk.CTkLabel(master=self, text="Enter Deposit Amount")
        L2.pack(pady=5)
        self.E2 = ctk.CTkEntry(master=self)
        self.E2.pack(pady=5)
        B1 = ctk.CTkButton(master=self, text="Deposit", command=self.deposit)
        B1.pack(pady=20)
        B2 = ctk.CTkButton(master=self, text="Back", command=self.back_to_main)
        B2.pack(pady=20)
        

    def deposit(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='faiz', database='faizdata')
        crsr = mydb.cursor()
        try:
            accno=self.E1.get()
            deposit=self.E2.get()
            
            sql="update accounts set balance=balance+"+deposit+" where Account_Number="+accno
            
            crsr.execute(sql)
            mydb.commit()
            messagebox.showinfo('Withdrawal','Amount Deposited Successfully!')
            
        except Exception as e:
            messagebox.showerror('Error',f"Failed to deposit amount: {e}")
            mydb.rollback()
            
        mydb.close()
        crsr.close()
        
    
    def back_to_main(self):
        self.destroy()
        self.master.deiconify()
   
        
class With_acc(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Withdrawal")
        self.geometry("250x350")

             

        L1 = ctk.CTkLabel(master=self, text="Enter Account Number")
        L1.pack(pady=5)
        self.E1 = ctk.CTkEntry(master=self)
        self.E1.pack(pady=5)

        L2 = ctk.CTkLabel(master=self, text="Enter Withdrawal Amount")
        L2.pack(pady=5)
        self.E2 = ctk.CTkEntry(master=self)
        self.E2.pack(pady=5)
        B1 = ctk.CTkButton(master=self, text="Withdraw", command=self.withdrawal)
        B1.pack(pady=20)
        B2 = ctk.CTkButton(master=self, text="Back", command=self.back_to_main)
        B2.pack(pady=20)

    def withdrawal(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='faiz', database='faizdata')
        crsr = mydb.cursor()
        try:
            accno=self.E1.get()
            withdrawal=self.E2.get()
            
            sql="update accounts set balance=balance-"+withdrawal+" where Account_Number="+accno+" and balance>="+withdrawal
            
            crsr.execute(sql)
            mydb.commit()
            messagebox.showinfo('Withdrawal','Amount Withdrawn Successfully!')
            
        except Exception as e:
            messagebox.showerror('Error',f"Failed to withdraw amount: {e}")
            mydb.rollback()
            
        mydb.close()
        crsr.close()
            
       
    def back_to_main(self):
        self.destroy()
        self.master.deiconify()
        
    
class Srch_acc(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Search Account")
        self.geometry("250x350")

             

        L1 = ctk.CTkLabel(master=self, text="Enter Account Number")
        L1.pack(pady=5)
        self.E1 = ctk.CTkEntry(master=self)
        self.E1.pack(pady=5)
        self.details = ctk.CTkLabel(self, text="")
        self.details.pack(pady=5)
        B1 = ctk.CTkButton(master=self, text="Search Account", command=self.search_account)
        B1.pack(pady=20)
        B2 = ctk.CTkButton(master=self, text="Back", command=self.back_to_main)
        B2.pack(pady=20)

    def search_account(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='faiz', database='faizdata')
        crsr = mydb.cursor()
        try:
            accno = self.E1.get()
            sql = "SELECT * FROM accounts WHERE Account_Number ="+accno
            crsr.execute(sql)
            record = crsr.fetchone()

            if record:
                details_text = f"Name: {record[1]}\nType: {record[2]}\nBalance: {record[3]}"
                self.details.configure(text=details_text)
            else:
                messagebox.showinfo("Not Found", "Account does not exist.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve account: {e}")
            
        mydb.close()
        crsr.close()
         
        
    def back_to_main(self):
        self.destroy()
        self.master.deiconify()
        
        
if __name__ == "__main__":
    app = Main_Window()
    app.mainloop()
