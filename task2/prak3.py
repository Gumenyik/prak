from tkinter import *
import math
def calcu(button):
    if button=='=':
        line.insert(END,'=' + str(eval(line.get())))
    elif button == "C":
        line.delete(0, END)
    elif button == "DEL":
        line.delete(len(str(line.get()))-1)
    elif button == "sin":
        line.insert(END, '=' + str(math.sin(int(line.get()))))
    elif button == "cos":
        line.insert(END, '=' + str(math.cos(int(line.get()))))
    elif button == "tan":
        line.insert(END, '=' + str(math.tan(int(line.get()))))
    elif button == "ctg":
        line.insert(END, '=' + str(math.ctg(int(line.get()))))
    elif button == "ln":
        line.insert(END, '=' + str(math.log(int(line.get()))))
    elif button == "log":
        line.insert(END, '=' + str(math.log10(int(line.get()))))
    elif button == "bin":
        line.insert(END, '=' + str(bin(int(line.get()))))
    else:
        if '=' in line.get():
            line.delete(0,END)
        line.insert(END,button)
        root.mainloop()
root=Tk()
root.title('Калькулятор')
root.geometry("530x510")
buttons=['=',"C", "DEL", "*", "/","%",
            "+","-", "1", "2", "3",
            'cos','sin',"4", "5","6", 
            'tan','ctg',"7", "8", "9",  
             'ln', 'log','bin', "0",              
             
             ]
x=417
y=5
for i in buttons:
    a=lambda x=i: calcu(x)
    Button(text=i,bg='#FFF',font=(20),command=a).place(x=x,y=y,height=80,width=100)
    x+=103
    if y>410 and x>300:
        x+=103
    if x>500:
        x=5
        y+=83
line = Entry(root, font=("Times New Roman", 30))
line.grid(row=0, column=0, columnspan=1)
line.place(x=5,y=5,height=75,width=408)
    








