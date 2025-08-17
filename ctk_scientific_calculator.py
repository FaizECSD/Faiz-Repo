import customtkinter as ctk
import math as m

# Parent Window/Screen
win=ctk.CTk()
win.geometry('750x350')
win.title('Scientific Calculator')

# Labels
L1=ctk.CTkLabel(master=win,text='Enter the Number')
L2=ctk.CTkLabel(master=win,text='Result')

# StringVars to store entry values
num_var=ctk.StringVar()
result_var=ctk.StringVar()

# TextFields/Entries
TF1=ctk.CTkEntry(master=win,textvariable=num_var)
TF2=ctk.CTkEntry(master=win,textvariable=result_var)

# Functions

def sqrt():
   try: 
       a = float(num_var.get()) 
       sqrt= m.sqrt(a) 
       result_var.set(sqrt) 
   except ValueError: 
       result_var.set("Invalid input")
    
def sin():
    try:
        a=float(num_var.get())
        sin=m.sin(a)
        result_var.set(sin)
    except ValueError:
        result_var.set('Invalid input')

def sinh():
   try:
       a=float(num_var.get())
       sinh=m.sinh(a)
       result_var.set(sinh)
   except ValueError:
        result_var.set('Invalid input')
        
def cosh():
   try:
       a=float(num_var.get())
       cosh=m.cosh(a)
       result_var.set(cosh)
   except ValueError:
        result_var.set('Invalid input')
        
def tanh():
    try:
        a=float(num_var.get())
        tanh=m.tanh(a)
        result_var.set(tanh)
    except ValueError:
        result_var.set('Invalid input')
                
def cos():
    try:
        a=float(num_var.get())
        cos=m.cos(a)
        result_var.set(cos)
    except ValueError:
        result_var.set('Invalid input')
        
def tan():
    try:
        a=float(num_var.get())
        if a!=90:
            tan=m.tan(float(a))
            result_var.set(tan)    
        else:
            result_var.set('Not Defined')
    except ValueError:
        result_var.set('Invalid input')
            
def factorial():
   try:
       a=int(num_var.get())
       f=1
       for i in range(1,a+1):
           f=f*i
       result_var.set(f)
   except ValueError:
       result_var.set('Invalid input')
              
def square():
    try:
        a=float(num_var.get())
        sq=a**2
        result_var.set(sq)
    except ValueError:
        result_var.set('Invalid input')
        
def cube():
    try:
        a=float(num_var.get())
        sq=a**3
        result_var.set(sq)
    except ValueError:
        result_var.set('Invalid input')
           
def log():
    try:
        a=float(num_var.get())
        log=m.log10(a)
        result_var.set(log)
    except ValueError:
        result_var.set('Invalid input')
    
def radian():
   try:
       a=float(num_var.get())
       rad=m.radians(a)
       result_var.set(rad)
   except ValueError:
       result_var.set('Invalid input')
    
def exponent():
    try:
        a=float(num_var.get())
        exp=m.exp(a)
        result_var.set(exp)
    except ValueError:
        result_var.set('Invalid input')

def reciprocal():
    try:
        a=float(num_var.get())
        rec=a**(-1)
        result_var.set(rec)
    except ValueError:
        result_var.set('Invalid input')

# Buttons
Bsqrt=ctk.CTkButton(master=win,text='sqrt',command=sqrt)
Bsin=ctk.CTkButton(master=win,text='sin',command=sin)
Bcos=ctk.CTkButton(master=win,text='cos',command=cos)
Btan=ctk.CTkButton(master=win,text='tan',command=tan)
Bsinh=ctk.CTkButton(master=win,text='sinh',command=sinh)
Bcosh=ctk.CTkButton(master=win,text='cosh',command=cosh)
Btanh=ctk.CTkButton(master=win,text='tanh',command=tanh)
Bfact=ctk.CTkButton(master=win,text='x!',command=factorial)
Bsq=ctk.CTkButton(master=win,text='x^2',command=square)
Bcube=ctk.CTkButton(master=win,text='x^3',command=cube)
Blog=ctk.CTkButton(master=win,text='log10',command=log)
Brad=ctk.CTkButton(master=win,text='Rad',command=radian)
Bexp=ctk.CTkButton(master=win,text='e^',command=exponent)
Brec=ctk.CTkButton(master=win,text='1/x',command=reciprocal)

# Placement
L1.place(x=170,y=20);  TF1.place(x=320,y=20)
L2.place(x=170,y=50);  TF2.place(x=320,y=50)

Bsq.place(x=100,y=100); Bcube.place(x=300,y=100); Brec.place(x=500,y=100)
Bsin.place(x=100,y=130); Bcos.place(x=300,y=130); Btan.place(x=500,y=130)
Bsinh.place(x=100,y=160); Bcosh.place(x=300,y=160); Btanh.place(x=500,y=160)
Bfact.place(x=100,y=190); Blog.place(x=300,y=190); Bexp.place(x=500,y=190)
Bsqrt.place(x=100,y=220); Brad.place(x=300,y=220)

Bexit=ctk.CTkButton(master=win,text='EXIT',command=win.destroy)
Bexit.place(x=300,y=300)

win.mainloop()

