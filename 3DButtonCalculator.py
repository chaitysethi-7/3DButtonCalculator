from tkinter import *
import tkinter as tk
import math
import tkinter.messagebox as mbox
from tkinter import Menu
import tkinter
import webbrowser

#COLORS AND BUTTON EFFECTS
lightgrey = "7E7873"
eerieblack = "#1C1C1C"
darkgrey = "#505050"
vividorange = "#FF9500"
applered = "#ca3302"
lightcream = "#f6bc80"
shoebrown = "#8e541c"
gray = "7d7c84"
darkdarkgray ="#333333"
black ="#000000"
lightred ="#FF474C"
darkred = "#9e0411"
rust = "#C26808"
#rust = "#FF5B00"
lightorange = "#Fa8100"
blue ="#006AFF"
lightblue="#4d97ff"
darkblue = "#002aff"

root = Tk()
root.title("3D Button Scientific Calculator by Chaitanya Sethi")
root.configure(background= eerieblack)
root.resizable(width = False, height =False)
root.geometry("904x522+0+0")


switch=None
calc = Frame(root)
calc.grid()

class Calc():
    def __init__ (self):
        self.total=0
        self.current=""
        self.input_value=TRUE
        self.check_sum = FALSE
        self.op = ""
        self.result=FALSE

    def numberEnter(self,num):
        self.result =  FALSE
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
    
    def Clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value =True

    def all_Clear_entry(self):
        self.Clear_entry()
        self.total = "0"
    
    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
    
    def sqr(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
        
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
    
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
    
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "power":
            self.total **= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
    
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
    
    def cos(self):
        self.result = False
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)
    
    def sin(self):
        self.result = False
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(float(txtDisplay.get()))
        self.display(self.current)
    
    def sinh(self):
        self.result = False
        self.current = math.sinh(float(txtDisplay.get()))
        self.display(self.current)
    
    def tanh(self):
        self.result = False
        self.current = math.tanh(float(txtDisplay.get()))
        self.display(self.current)
    
    def acos(self):
        self.result = False
        try:
            value = float(txtDisplay.get())
            if abs(value) > 1.0:
                raise ValueError("Value out of range")
            self.current = math.acos(value)
            self.display(self.current)
        except ValueError:
            tkinter.messagebox.showerror("Domain Error", "Check values and operators")

    def asin(self):
        self.result = False
        try:
            value = float(txtDisplay.get())
            if abs(value) > 1.0:
                raise ValueError("Value out of range")
            self.current = math.asin(value)
            self.display(self.current)
        except ValueError:
            tkinter.messagebox.showerror("Domain Error", "Check values and operators")


    def atan(self):
        self.result = False
        self.current = math.atan(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    
    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)
    
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
    
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)
    
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)
    
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
    
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def exp2(self):
        self.result = False
        self.current = math.exp2(float(txtDisplay.get()))
        self.display(self.current)
    
    def exp10(self):
        self.result = False
        self.current = math.exp10(float(txtDisplay.get()))
        self.display(self.current)
    
    def reciprocal(self):
        self.result = False
        try:
            value = float(txtDisplay.get())
            if value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            self.current = 1 / value
            self.display(self.current)
        except (ValueError, ZeroDivisionError):
            tkinter.messagebox.showerror("Error", "Invalid input or division by zero") #calculate power of x raised to y

    def modulo(self):
        self.result = False
        try:
            value = float(txtDisplay.get())
            divisor = float(input("Enter divisor: "))  # Assuming you take divisor as input
            self.current = value % divisor
            self.display(self.current)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input")

    def power(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get(),self.current))
        self.display(self.current)
    
    def exp10(self):
        self.result = False
        try:
            exponent = float(txtDisplay.get())
            self.current = 10 ** exponent
            self.display(self.current)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input")

    def factorial(self):
        self.result = False
        try:
            value = int(txtDisplay.get())
            if value < 0:
                raise ValueError("Factorial is not defined for negative numbers")
            self.current = math.factorial(value)
            self.display(self.current)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input or factorial not defined for negative numbers")

def del_clicked(): 
    pos = len(txtDisplay.get()) 
    display = str(txtDisplay.get()) 
    if display == '': 
        txtDisplay.insert(0, '0') 
    elif display == ' ': 
        txtDisplay.insert(0, '0') 
    elif display == '0': 
        pass 
    else: 
        txtDisplay.delete(0, END) 
        txtDisplay.insert(0, display[0:pos-1]) 
     

#FOR HOVERING====================
def on_enter(event):
    event.widget.config(bg=darkdarkgray)

def on_leave(event):
    event.widget.config(bg=darkgrey)

def on_enter_clear(event):
    event.widget.config(bg=lightgrey)

def on_leave_clear(event):
    event.widget.config(bg=darkgrey)

def on_enter_del(event):
    event.widget.config(bg=lightblue)

def on_leave_del(event):
    event.widget.config(bg=blue)

def on_enter_op(event):
    event.widget.config(bg=lightorange)

def on_leave_op(event):
    event.widget.config(bg=vividorange)

added_value = Calc()

txtDisplay = Entry(calc, font=('Verdana',30),fg="WHITE", bg=eerieblack, bd=13,width=18,justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4,pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i =0
btn = []
for j in range (3,6):
    for k in range(3):
        btn.append(Button(calc,width=4,height=1, font=('Verdana',25),fg="WHITE", bg=darkgrey, bd=10, activebackground=black, activeforeground="WHITE", text=numberpad[i]))
        btn[i].grid(row=j, column=k,pady=1)
        btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
        btn[i].bind("<Enter>", on_enter)
        btn[i].bind("<Leave>", on_leave)
        i+=1


#================STANDARD CALCULATOR BUTTONS=============================#=

#Clear Buttons
btnclear = Button(calc, text='C', width=4, height=1, font=('Verdana', 23, 'bold'), 
                  fg="WHITE", bg=blue, bd=10, 
                  activebackground=darkblue,activeforeground="white")
btnclear.grid(row=2, column=0, pady=1)
btnclear['command'] = added_value.Clear_entry
btnclear.bind("<Enter>", on_enter_del)
btnclear.bind("<Leave>", on_leave_del)

btnAllclear = Button(calc, text='CE', width=4, height=1, font=('Verdana', 23, 'bold'), fg="WHITE", bg=blue, bd=10, activebackground=darkblue,activeforeground="white", command=added_value.all_Clear_entry)
btnAllclear.grid(row=2, column=1, pady=1)
btnAllclear.bind("<Enter>", on_enter_del)
btnAllclear.bind("<Leave>", on_leave_del)

#Operation Buttons
btnAdd = Button(calc,text='+',width=4,height=1, font=('Verdana',25),fg="WHITE", bg=vividorange, bd=10, activebackground=rust, activeforeground="WHITE", command = lambda: added_value.operation("add"))
btnAdd.grid(row=2,column=3,pady=1)
btnAllclear.grid(row=2, column=1, pady=1)
btnAdd.bind("<Enter>", on_enter_op)
btnAdd.bind("<Leave>", on_leave_op)

# Button Subtraction
btnSub = Button(calc, text='-', width=4, height=1, font=('Verdana', 25), fg="WHITE", bg=vividorange, bd=10, activebackground=rust, activeforeground="WHITE", command=lambda: added_value.operation("sub"))
btnSub.grid(row=3, column=3, pady=1)
btnSub.bind("<Enter>", on_enter_op)
btnSub.bind("<Leave>", on_leave_op)

# Button Multiplication
btnMult = Button(calc, text='x', width=4, height=1, font=('Verdana', 25), fg="WHITE", bg=vividorange, bd=10, activebackground=rust, activeforeground="WHITE", command=lambda: added_value.operation("multi"))
btnMult.grid(row=4, column=3, pady=1)
btnMult.bind("<Enter>", on_enter_op)
btnMult.bind("<Leave>", on_leave_op)

# Button Division
btnDiv = Button(calc, text='÷', width=4, height=1, font=('Verdana', 25), fg="WHITE", bg=vividorange, bd=10, activebackground=rust, activeforeground="WHITE", command=lambda: added_value.operation("divide"))
btnDiv.grid(row=5, column=3, pady=1)
btnDiv.bind("<Enter>", on_enter_op)
btnDiv.bind("<Leave>", on_leave_op)

# Button Equals
btnEquals = Button(calc, text='=', width=4, height=1, font=('Verdana', 25), fg="WHITE", bg=vividorange, bd=10, activebackground="#FF5349", activeforeground="WHITE", command=added_value.sum_of_total)
btnEquals.grid(row=6, column=3, pady=1)
btnEquals.bind("<Enter>", on_enter_op)
btnEquals.bind("<Leave>", on_leave_op)

#Remaining Buttons
btnZero = Button(calc,text='0',width=4,height=1, font=('Verdana',25),fg="WHITE", bg=darkgrey, activebackground=black, activeforeground="WHITE", bd=10, command = lambda: added_value.numberEnter(0))
btnZero.grid(row=6,column=1,pady=1)
btnZero.bind("<Enter>", on_enter)
btnZero.bind("<Leave>", on_leave)

# Button Dot
btnDot = Button(calc, text='.', width=4, height=1, font=('Verdana', 25), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=lambda: added_value.numberEnter("."))
btnDot.grid(row=6, column=2, pady=1)
btnDot.bind("<Enter>", on_enter)
btnDot.bind("<Leave>", on_leave)

# Button Plus/Minus
btnPlusMinus = Button(calc, text='±', width=4, height=1, font=('Proxima Nova', 25), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.mathsPM)
btnPlusMinus.grid(row=2, column=2, pady=1)
btnPlusMinus.bind("<Enter>", on_enter)
btnPlusMinus.bind("<Leave>", on_leave)


btnDelete= Button(calc,text='DEL',width=4,height=1, font=('Verdana',23,'bold'),fg="WHITE", bg=blue, bd=10, activebackground=darkblue, activeforeground="WHITE",command = del_clicked)
btnDelete.grid(row=6,column=0,pady=1)
btnDelete.bind("<Enter>", on_enter_del)
btnDelete.bind("<Leave>", on_leave_del)

#=================SCIENTIFIC CALCULATOR BUTTONS====================================

#Operation Buttons Row 1
btnPi = Button(calc, text='π', width=4, height=1, font=('Arial',25), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.pi)
btnPi.grid(row=2, column=4, pady=1)
btnPi.bind("<Enter>", on_enter)
btnPi.bind("<Leave>", on_leave)

btnCos = Button(calc, text='cos', width=4, height=1, font=('Verdana',24), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.cos)
btnCos.grid(row=2, column=5, pady=1)
btnCos.bind("<Enter>", on_enter)
btnCos.bind("<Leave>", on_leave)

btntan = Button(calc, text='tan', width=4, height=1, font=('Verdana',24), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.tan)
btntan.grid(row=2, column=6, pady=1)
btntan.bind("<Enter>", on_enter)
btntan.bind("<Leave>", on_leave)

btnsin = Button(calc, text='sin', width=4, height=1, font=('Verdana',24), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.sin)
btnsin.grid(row=2, column=7, pady=1)
btnsin.bind("<Enter>", on_enter)
btnsin.bind("<Leave>", on_leave)

#Operation Buttons Row 2
btnE = Button(calc, text='e', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.e)
btnE.grid(row=3, column=4, pady=1)
btnE.bind("<Enter>", on_enter)
btnE.bind("<Leave>", on_leave)

btnCosh = Button(calc, text='cosh', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.cosh)
btnCosh.grid(row=3, column=5, pady=1)
btnCosh.bind("<Enter>", on_enter)
btnCosh.bind("<Leave>", on_leave)

btntanh = Button(calc, text='tanh', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.tanh)
btntanh.grid(row=3, column=6, pady=1)
btntanh.bind("<Enter>", on_enter)
btntanh.bind("<Leave>", on_leave)

btnsinh = Button(calc, text='sinh', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.sinh)
btnsinh.grid(row=3, column=7, pady=1)
btnsinh.bind("<Enter>", on_enter)
btnsinh.bind("<Leave>", on_leave)

#Operation Buttons Row 3
btnln = Button(calc, text='ln', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.log)
btnln.grid(row=4, column=4, pady=1)
btnln.bind("<Enter>", on_enter)
btnln.bind("<Leave>", on_leave)

btnaCos = Button(calc, text='acos', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.acos)
btnaCos.grid(row=4, column=5, pady=1)
btnaCos.bind("<Enter>", on_enter)
btnaCos.bind("<Leave>", on_leave)

btnaTan = Button(calc, text='atan', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.atan)
btnaTan.grid(row=4, column=6, pady=1)
btnaTan.bind("<Enter>", on_enter)
btnaTan.bind("<Leave>", on_leave)

btnaSin = Button(calc, text='asin', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.asin)
btnaSin.grid(row=4, column=7, pady=1)
btnaSin.bind("<Enter>", on_enter)
btnaSin.bind("<Leave>", on_leave)

btnlog2 = Button(calc, text='log₂', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.log2)
btnlog2.grid(row=5, column=4, pady=1)
btnlog2.bind("<Enter>", on_enter)
btnlog2.bind("<Leave>", on_leave)

btnexp = Button(calc, text='eˣ', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.exp)
btnexp.grid(row=5, column=5, pady=1)
btnexp.bind("<Enter>", on_enter)
btnexp.bind("<Leave>", on_leave)

btnpow = Button(calc, text='xʸ', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=lambda: added_value.operation("power"))
btnpow.grid(row=5, column=6, pady=1)
btnpow.bind("<Enter>", on_enter)
btnpow.bind("<Leave>", on_leave)

btnfact = Button(calc, text='x!', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.factorial)
btnfact.grid(row=5, column=7, pady=1)
btnfact.bind("<Enter>", on_enter)
btnfact.bind("<Leave>", on_leave)
#Operation Buttons Row 4
btnndeg = Button(calc, text='deg', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.degrees)
btnndeg.grid(row=6, column=5, pady=1)
btnndeg.bind("<Enter>", on_enter)
btnndeg.bind("<Leave>", on_leave)

btnrad = Button(calc, text='rad', width=4, height=1, font=('Verdana', 21), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.radians)
btnrad.grid(row=6, column=6, pady=1)
btnrad.bind("<Enter>", on_enter)
btnrad.bind("<Leave>", on_leave)

btn2rx = Button(calc, text='2ˣ', width=4, height=1, font=('Verdana', 21), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.exp2)
btn2rx.grid(row=6, column=7, pady=1)
btn2rx.bind("<Enter>", on_enter)
btn2rx.bind("<Leave>", on_leave)

#Operation Buttons Row 5
btnlog10 = Button(calc, text='log₁₀', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.log10)
btnlog10.grid(row=6, column=4, pady=1)
btnlog10.bind("<Enter>", on_enter)
btnlog10.bind("<Leave>", on_leave)

btninv = Button(calc, text='1/x', width=4, height=1, font=('Verdana',22), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.reciprocal)
btninv.grid(row=6, column=5, pady=1)
btninv.bind("<Enter>", on_enter)
btninv.bind("<Leave>", on_leave)

btnSqrt = Button(calc, text='√x', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.sqr)
btnSqrt.grid(row=6, column=6, pady=1)
btnSqrt.bind("<Enter>", on_enter)
btnSqrt.bind("<Leave>", on_leave)

btn10x = Button(calc, text='10ˣ', width=4, height=1, font=('Verdana',23), fg="WHITE", bg=darkgrey, bd=10, activebackground="black", activeforeground="WHITE", command=added_value.exp10)
btn10x.grid(row=6, column=7, pady=1)
btn10x.bind("<Enter>", on_enter)
btn10x.bind("<Leave>", on_leave)

lblDisplay = Label(calc, text="Scientific Functions", font=("Verdana", 22,'bold'), bd=10,width=20, height=2, justify="center", border=5, fg="WHITE", bg=lightorange, relief="solid")
lblDisplay.grid(row=0, column=4, columnspan=4)

#==================Menu and function================================

# Function to copy the calculator display content to the clipboard
menubar = Menu(calc)
def copy_content():
    content = txtDisplay.get()
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(content)  # Append the content to the clipboard

# Function to cut the calculator display content and copy it to the clipboard
def cut_content():
    copy_content()  # Call the copy_content function to copy the content
    txtDisplay.delete(0, tk.END)  # Delete the content from the calculator display

# Function to paste the content from the clipboard into the calculator display
def paste_content():
    content = root.clipboard_get()  # Get the content from the clipboard
    txtDisplay.insert(tk.END, content)  # Insert the content into the calculator display

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return 

def Scientific():
    root.resizable(width = False, height =False)
    root.geometry("904x522+0+0")
    
def Standard():
    root.resizable(width = False, height =False)
    root.geometry("479x522+0+0")

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu = filemenu)
filemenu.add_command(label = "Standard", command =Standard)
filemenu.add_command(label = "Scientific", command =Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command =iExit)


# Create the Edit menu
edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

# Add Cut, Copy, Paste menu items
edit_menu.add_command(label="Cut", command=cut_content)
edit_menu.add_command(label="Copy", command=copy_content)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste_content)

def open_help():
    url = "https://docs.google.com/document/d/1xVcBHU6gMerKjVES1oMzdwpUM5mR53FYL-DiWXbyGNA/edit#heading=h.8ksy53crcpr1"
    webbrowser.open_new(url)

# Create the Help menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="View Help", command=open_help)

root.configure(menu=menubar)

root.mainloop()