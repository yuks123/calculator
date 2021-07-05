import tkinter as tk


def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val=""
    data.set("")



def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)


app=tk.Tk()
app.title("Calculator")
app.geometry("275x145")
val=""
data=tk.StringVar()
display=tk.Entry(app,textvariable=data,bd=25,justify="right",bg="skyblue",font=("ariel",20))
display.grid(row=0,columnspan=7)



btn7=tk.Button(app,text="7",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('7'))
btn7.grid(row=1,column=0)

btn8=tk.Button(app,text="8",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('8'))
btn8.grid(row=1,column=1)

btn9=tk.Button(app,text="9",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('9'))
btn9.grid(row=1,column=2)

btn_add=tk.Button(app,text="+",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('+'))
btn_add.grid(row=1,column=3)



btn4=tk.Button(app,text="4",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('4'))
btn4.grid(row=2,column=0)

btn5=tk.Button(app,text="5",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('5'))
btn5.grid(row=2,column=1)

btn6=tk.Button(app,text="6",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('6'))
btn6.grid(row=2,column=2)

btn_sub=tk.Button(app,text="-",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('-'))
btn_sub.grid(row=2,column=3)


btn1=tk.Button(app,text="1",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('1'))
btn1.grid(row=3,column=0)

btn2=tk.Button(app,text="2",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('2'))
btn2.grid(row=3,column=1)

btn3=tk.Button(app,text="3",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('3'))
btn3.grid(row=3,column=2)

btn_multiply=tk.Button(app,text="*",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('*'))
btn_multiply.grid(row=3,column=3)


btnc=tk.Button(app,text="C",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClear())
btnc.grid(row=4,column=0)

btn0=tk.Button(app,text="0",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('0'))
btn0.grid(row=4,column=1)



btn_equal=tk.Button(app,text="=",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnEquals())
btn_equal.grid(row=4,column=2)

btn_divide=tk.Button(app,text="/",font=("Ariel",9,"bold"),bd=12,height=2,width=7,command=lambda:btnClick('/'))
btn_divide.grid(row=4,column=3)










app.mainloop()
