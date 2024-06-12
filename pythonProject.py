from tkinter import *
import math
import threading

exp="" #defines global variable exp and assigns it a default value

#Function that uses threading to speed up execution
def threadingFunc(function):
    thread = threading.Thread(target=function)
    thread.start()

#Function that adds to global variable exp whatever is displayed in the label
def addToexp(): 
    global exp    
    exp+=lbl.cget("text")
    return exp

#Function that adds answer to specific calculations to global variable exp
def addToexp2(ans):
    global exp
    exp+=str(ans)
    return exp
  
#Function used to find out the square of a number using built-in function pow()
def Sqr():
    def calc_sqr():
        global exp
        if "." in str(lbl.cget("text")):
            ans=pow(float(lbl.cget("text")),2)
        else:
            ans=pow(int(lbl.cget("text")),2)
            
        if str(lbl.cget("text")) in exp: #removes number given to change to square of number
            exp=exp.replace(str(lbl.cget("text")),"")
        lbl.configure(text=str(ans))
        addToexp2(ans) #Adds answer to expression
    
    threadingFunc(calc_sqr) #Uses threadingFunc to speed up calculation
    
#Function used to find out the cube of a number using built-in function pow()    
def Cube():
    def calc_cube():
        global exp
        if "." in str(lbl.cget("text")):
            ans=pow(float(lbl.cget("text")),3)
        else:
            ans=pow(int(lbl.cget("text")),3)
            
        if str(lbl.cget("text")) in exp: #removes number given to change to cube of number
            exp=exp.replace(str(lbl.cget("text")),"")
        lbl.configure(text=str(ans))
        addToexp2(ans) #Adds answer to expression
    
    threadingFunc(calc_cube) #Uses threadingFunc to speed up calculation

#Function used to find sqaure root of number using built-in function sqrt()
def Sqrt():
    def calc_sqrt():
        global exp
        if "." in str(lbl.cget("text")):
            ans=math.sqrt(float(lbl.cget("text"))) #rounds the result to 0 decimal places
        else:
            ans=round(math.sqrt(int(lbl.cget("text"))))
            
        if lbl.cget("text") in exp: #removes number given to change to sqaure root of number
            exp=exp.replace(lbl.cget("text"),"")
        lbl.configure(text=str(ans))
        addToexp2(ans) #Adds answer to expression
        
    threadingFunc(calc_sqrt) #Uses threadingFunc to speed up calculation

#Function used to find cube root of number using built-in function pow()
def Cbrt():
    def calc_cbrt():
        global exp
        if "." in str(lbl.cget("text")):
            ans=pow(float(lbl.cget("text")),1/3) #Finds cube root of number using 1/3 as exponent
        else:
            ans=round(pow(int(lbl.cget("text")),1/3))
            
        if str(lbl.cget("text")) in exp: #removes number given to change to cube root of number
            exp=exp.replace(str(lbl.cget("text")),"")
        lbl.configure(text=str(ans))
        addToexp2(ans) #Adds answer to expression
        
    threadingFunc(calc_cbrt) #Uses threadingFunc to speed up calculation

#Function used to add 7 to expression
def Seven():
    lbl.configure(text="7")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 8 to expression
def Eight():
    lbl.configure(text="8")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 9 to expression
def Nine():
    lbl.configure(text="9")
    addToexp()
    lbl.configure(text=exp)

#Function used to add "+" to expression
def Plus():
    lbl.configure(text="+")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 4 to expression
def Four():
    lbl.configure(text="4")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 5 to expression
def Five():
    lbl.configure(text="5")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 6 to expression
def Six():
    lbl.configure(text="6")
    addToexp()
    lbl.configure(text=exp)

#Function used to add "-" to expression
def Minus():
    lbl.configure(text="-")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 1 to expression
def One():
    lbl.configure(text="1")
    addToexp()
    lbl.configure(text=exp)

#Function used to add 2 to expression
def Two():
    lbl.configure(text="2")
    addToexp()
    lbl.configure(text=exp)
 
#Function used to add 3 to expression
def Three():
    lbl.configure(text="3")
    addToexp()
    lbl.configure(text=exp)
    
#Function used to add "*" to expression
def Multiply():
    lbl.configure(text="*")
    addToexp()
    lbl.configure(text=exp)

#Function used to clear the expression (to start new calculation)
def Clear():
    global exp
    exp=""
    lbl.configure(text="")
    addToexp()

#Function used to add 0 to expression
def Zero():
    lbl.configure(text="0")
    addToexp()
    lbl.configure(text=exp)

#Function used to find answer using the function eval()
def Equal():
    try:
        global exp
        ans=eval(exp) #converts global variable eq to expression and computes answer
        lbl.configure(text=ans)
        exp=str(ans)
    except:
        lbl.configure(text="Error") #Displays error message in case of any error

#Function used to add "/" to expression
def Div():
    lbl.configure(text="/")
    addToexp()
    lbl.configure(text=exp)
    
#Function used to add "%" to expression
def Percentage():
    global exp
    value = float(lbl.cget("text"))
    if str(lbl.cget("text")) in exp:
        exp=exp.replace(str(lbl.cget("text")),"")
    lbl.configure(text=str(value/100))
    addToexp()

#Function used to add power to expression
def Power():
    global exp
    global base
    base = lbl.cget("text")
    if str(lbl.cget("text")) in exp:
        exp=exp.replace(str(lbl.cget("text")),"")
    lbl.configure(text=str(base)+"**")
    addToexp()

#Function used to add decimal to expression
def Decimal():
    global exp
    current_val=str(lbl.cget("text"))
    if current_val[-1] != ".":
        if current_val in exp:
            exp=exp.replace(current_val,"")
    lbl.configure(text=current_val+".")
    addToexp()

#Function used to calculate the reciprocal (1/x) of the expression
def OneOverX():
    global exp
    value = float(lbl.cget("text"))
    if value != 0:
        if str(lbl.cget("text")) in exp:
            exp=exp.replace(str(lbl.cget("text")),"")
        lbl.configure(text=str(1/value))
        addToexp()
    else:
        lbl.configure(text="Cannot divide by Zero")

#Function used to remove the last entered character or digit from the expression 
def Backspace():
    global exp
    exp=exp[:-1]
    lbl.configure(text=exp)

#Function used to compute the sine of the angle entered and displays the result    
def Sin():
    def calc_sin():
        try:
            global exp
            angle = float(lbl.cget("text"))
            ans = math.sin(math.radians(angle))# Convert angle to radians
            if lbl.cget("text") in exp:
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans)
        except:
            lbl.configure(text="Error")
    
    threadingFunc(calc_sin) #Uses threadingFunc to speed up calculation

#Function used to compute the cosine of the angle entered and displays the result 
def Cos():
    def calc_cos():
        try:
            global exp
            angle = float(lbl.cget("text"))
            ans = math.cos(math.radians(angle))  # Convert angle to radians
            if lbl.cget("text") in exp:
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans)
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_cos) #Uses threadingFunc to speed up calculation

#Function used to compute the tangent of the angle entered and displays the result 
def Tan():
    def calc_tan():
        try:
            global exp
            angle = float(lbl.cget("text"))
            ans = math.tan(math.radians(angle))  # Convert angle to radians
            if lbl.cget("text") in exp:
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans)
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_tan) #Uses threadingFunc to speed up calculation

#Function used to convert decimal to binary number using built-in function bin()
def Bin():
    def calc_bin():
        try:
            global exp
            ans=bin(int(lbl.cget("text")))
            if lbl.cget("text") in exp: #removes number given to change to it's binary form
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans) #Adds answer to expression
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_bin) #Uses threadingFunc to speed up calculation

#Function used to convert decimal to hexadecimal number using built-in function hex()
def Hex(): 
    def calc_hex():
        try:
            global exp
            ans=hex(int(lbl.cget("text")))
            if lbl.cget("text") in exp: #removes number given to change to it's binary form
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans) #Adds answer to expression
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_hex) #Uses threadingFunc to speed up calculation

#Function used to find logarithm of number using math function log10()
def Log():
    def calc_log():
        try:
            global exp
            ans=math.log10(int(lbl.cget("text")))
            if lbl.cget("text") in exp: #removes number given to change to it's logarithm
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans) #Adds answer to expression
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_log) #Uses threadingFunc to speed up calculation

#Function used to add opening bracket
def Left():
    lbl.configure(text="(")
    addToexp()
    lbl.configure(text=exp)

#Function used to add closing bracket
def Right():
    lbl.configure(text=")")
    addToexp()
    lbl.configure(text=exp)

#Function used to convert binary, hexadecimal or octal number to decimal using int()
def Dec():
    def calc_dec():
        try:
            global exp
            ans=""
            if lbl.cget("text")[0:2] == "0x":
                ans=int(lbl.cget("text"),16) #int() with base 16
                
            elif lbl.cget("text")[0:2] == "0b":
                ans=int(lbl.cget("text"),2) #int() with base 2
                
            else:
                ans=int(lbl.cget("text"),8) #int() with base 8
                
            if lbl.cget("text") in exp: #removes number given to change to it's decimal form
                exp=exp.replace(lbl.cget("text"),"")
                
            lbl.configure(text=str(ans))
            addToexp2(str(ans)) #Adds answer to expression
            
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_dec) #Uses threadingFunc to speed up calculation

#Function used to convert decimal number to octal number using built-in function oct()
def Oct():
    def calc_oct():
        try:
            global exp
            ans=oct(int(lbl.cget("text")))
            if lbl.cget("text") in exp: #removes number given to change to it's octal form
                exp=exp.replace(lbl.cget("text"),"")
            lbl.configure(text=ans)
            addToexp2(ans) #Adds answer to expression
        except:
            lbl.configure(text="Error")
            
    threadingFunc(calc_oct) #Uses threadingFunc to speed up calculation

window=Tk(); #Creates main window for calculator
window.geometry('550x398') #Sets width and height of window
window.title("Calculator") #Sets title of window as 'Calculator'
window.iconbitmap("calc.ico") #Sets icon of calculator with given icon file

lbl = Label(window, text="0", bg="white", font=('MS Gothic', 40), bd=5) #Defines a label to display numbers or calculation results
lbl.grid(column=0, row=0) #Places label in the first column and row of window

'''ALL Buttons have the following attributes:
   master: window
   text: different for each button
   background color: black
   foreground color: gold
   width: 5
   font family: Gungsuh
   font size: 25
   command: different for each button
   
   Buttons are placed in the window using place() method'''
 

#Button 1: Displays 'x²' symbol and performs Sqr function when clicked
btn=Button(window, text="x\u00b2", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Sqr)
btn.place(x=0, y=90, anchor="w") #specifies position of button (top left corner is placed at given coordinates)

#Button 2: Displays 'x³' symbol and performs Cube function when clicked
btn=Button(window, text="x\u00b3", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Cube)
btn.place(x=90, y=90, anchor="w")

#Button 3: Displays '√' symbol and performs Sqrt function when clicked
btn=Button(window, text="\u221A", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Sqrt)
btn.place(x=180, y=90, anchor="w")

#Button 4: Displays '∛' symbol and performs Cbrt function when clicked
btn=Button(window, text="\u221B", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Cbrt)
btn.place(x=270, y=90, anchor="w")

#Button 5: Displays '7' and performs Seven function when clicked
btn=Button(window, text="7", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Seven)
btn.place(x=0, y=143, anchor="w")

#Button 6: Displays '8' and performs Eight function when clicked
btn=Button(window, text="8", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Eight)
btn.place(x=90, y=143, anchor="w")

#Button 7: Displays '9' and performs Nine function when clicked
btn=Button(window, text="9", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Nine)
btn.place(x=180, y=143, anchor="w")

#Button 8: Displays '+' and performs Plus function when clicked
btn=Button(window, text="+", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Plus)
btn.place(x=270, y=143, anchor="w")

#Button 9: Displays '4' and performs Four function when clicked
btn=Button(window, text="4", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Four)
btn.place(x=0, y=196, anchor="w")

#Button 10: Displays '5' and performs Five function when clicked
btn=Button(window, text="5", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Five)
btn.place(x=90, y=196, anchor="w")

#Button 11: Displays '6' and performs Six function when clicked
btn=Button(window, text="6", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Six)
btn.place(x=180, y=196, anchor="w")

#Button 12: Displays '-' and performs Minus function when clicked
btn=Button(window, text="-", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Minus)
btn.place(x=270, y=196, anchor="w")

#Button 13: Displays '1' and performs One function when clicked
btn=Button(window, text="1", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=One)
btn.place(x=0, y=246, anchor="w")

#Button 14: Displays '2' and performs Two function when clicked
btn=Button(window, text="2", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Two)
btn.place(x=90, y=246, anchor="w")

#Button 15: Displays '3' and performs Three function when clicked
btn=Button(window, text="3", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Three)
btn.place(x=180, y=246, anchor="w")

#Button 16: Displays '*' and performs Multiply function when clicked
btn=Button(window, text="x", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Multiply)
btn.place(x=270, y=246, anchor="w")

#Button 17: Displays 'C' and performs Clear function when clicked
btn=Button(window, text="C", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Clear)
btn.place(x=0, y=296, anchor="w")

#Button 18: Displays '0' and performs Zero function when clicked
btn=Button(window, text="0", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Zero)
btn.place(x=90, y=296, anchor="w")

#Button 19: Displays '=' and performs Equal function when clicked
btn=Button(window, text="=", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Equal)
btn.place(x=180, y=296, anchor="w")

#Button 20: Displays '/' and performs Div function when clicked
btn=Button(window, text="/", bg="black", fg="Gold", width=5,
           font=('Gungsuh', 25), command=Div)
btn.place(x=270, y=296, anchor="w")

#Button 21: Displays '%' and performs Percentage function when clicked
btn = Button(window, text="%", bg="black", fg="Gold", width=5,
            font=('Gungsuh', 25), command=Percentage)
btn.place(x=360, y=90, anchor="w")

#Button 22: Displays 'xʸ' and performs Power function when clicked
btn = Button(window, text="x\u02b8", bg="black", fg="Gold", width=5,
            font=('Gungsuh', 25), command=Power)
btn.place(x=360, y=143, anchor="w")

#Button 23: Displays '.' and performs Decimal function when clicked
btn = Button(window, text=".", bg="black", fg="Gold", width=5,
            font=('Gungsuh', 25), command=Decimal)
btn.place(x=360, y=196, anchor="w")

#Button 24: Displays '¹/ₓ' and performs Seven function when clicked
btn = Button(window, text="\u215f\u02e3", bg="black", fg="Gold", width=5,
            font=('Gungsuh', 25), command=OneOverX)
btn.place(x=360, y=246, anchor="w")

#Button 25: Displays '⌫' and performs Backspace function when clicked
btn = Button(window, text="\u232b", bg="black", fg="Gold", width=5,
            font=('Gungsuh', 25), command=Backspace)
btn.place(x=360, y=296, anchor="w")

#Button 26: Displays 'Sin' and performs Sin function when clicked
btn = Button(window, text="Sin", bg="black", fg="Gold", width=5,
             font=('Gungsuh', 25), command=Sin)
btn.place(x=450, y=90, anchor="w")

#Button 27: Displays 'Cos' and performs Cos function when clicked
btn=Button(window, text="Cos", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Cos)
btn.place(x=450, y=143, anchor="w")

#Button 28: Displays 'Tan' and performs Tan function when clicked
btn = Button(window, text="Tan", bg="black", fg="Gold", width=5,
             font=('Gungsuh', 25), command=Tan)
btn.place(x=450, y=196, anchor="w")

#Button 29: Displays 'Bin' and performs Bin function when clicked
btn=Button(window, text="Bin", bg="black", fg="Gold", width=5, 
           font=('Gungsuh', 25), command=Bin)
btn.place(x=450, y=246, anchor="w")

#Button 30: Displays 'Hex' and performs Hex function when clicked
btn = Button(window, text="Hex", bg="black", fg="Gold", width=5,
             font=('Gungsuh', 25), command=Hex)
btn.place(x=450, y=296, anchor="w")

#Button 31: Displays 'Log' and performs Log function when clicked
btn = Button(window, text="log", bg="black", fg="Gold", width=9,
             font=('Gungsuh',25), command=Log)
btn.place(x=0, y=363, anchor="w")

#Button 32: Displays '(' and performs Left function when clicked
btn = Button(window, text="(", bg="black", fg="Gold", width=5,
             font=('Gungsuh',25), command=Left)
btn.place(x=180, y=363, anchor="w")

#Button 33: Displays ')' and performs Right function when clicked
btn = Button(window, text=")", bg="black", fg="Gold", width=5,
             font=('Gungsuh',25), command=Right)
btn.place(x=270, y=363, anchor="w")

#Button 34: Displays 'Dec' and performs Dec function when clicked
btn = Button(window, text="Dec", bg="black", fg="Gold", width=5,
             font=('Gungsuh',25), command=Dec)
btn.place(x=360, y=363, anchor="w")

#Button 35: Displays 'Oct' and performs Oct function when clicked
btn = Button(window, text="Oct", bg="black", fg="Gold", width=5,
             font=('Gungsuh',25), command=Oct)
btn.place(x=450, y=363, anchor="w")

#Starts the event loop or runs the application
window.mainloop()