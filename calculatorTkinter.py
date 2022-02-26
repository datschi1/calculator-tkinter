from tkinter import *
import parser

from click import command

root = Tk()
root.title("Calculator")

#place user input in the entry
#i is index, num is the button number that will be passed though the function, when button is
#pressed number is shown and i goes from 0 to 1 index and so one, so you can type multiple nums
i = 0
def get_num(num):
    global i 
    enter.insert(i,num)
    i+=1

def get_operation(operator):
    global i 
    length = len(operator)
    enter.insert(i,operator)
    i+=length

def calculate():
    entire_str = enter.get()
    try:
        a = parser.expr(entire_str).compile()
        result = eval(a)
        del_all()
        enter.insert(0,result)
    except Exception:
        del_all()
        enter.insert(0,"error")

def del_all():
    enter.delete(0,END)

def undo():
    entire_str = enter.get()
    if len(entire_str):
        new_str = entire_str[:-1]
        del_all()
        enter.insert(0,new_str)
    else:
        del_all()
        enter.insert(0,"Error")


#added the field where numbers are present
enter = Entry(root)
enter.grid(row = 1,columnspan=6,sticky=W+E)
#adding buttons
Button(root, text = "1",command=lambda:get_num(1)).grid(row=2,column=0)
Button(root, text = "2",command=lambda:get_num(2)).grid(row=2,column=1)
Button(root, text = "3",command=lambda:get_num(3)).grid(row=2,column=2)

Button(root, text = "4",command=lambda:get_num(4)).grid(row=3,column=0)
Button(root, text = "5",command=lambda:get_num(5)).grid(row=3,column=1)
Button(root, text = "6",command=lambda:get_num(6)).grid(row=3,column=2)

Button(root, text = "7",command=lambda:get_num(7)).grid(row=4,column=0)
Button(root, text = "8",command=lambda:get_num(8)).grid(row=4,column=1)
Button(root, text = "9",command=lambda:get_num(9)).grid(row=4,column=2)

#other buttons
Button(root,text = "AC",command=lambda:del_all()).grid(row = 5,column=0)
Button(root,text = "0",command=lambda:get_num(0)).grid(row = 5,column=1)
Button(root,text = "=",command=lambda:calculate()).grid(row = 5,column=2)

Button(root,text = "+",command=lambda:get_operation("+")).grid(row = 2,column=3)
Button(root,text = "-",command=lambda:get_operation("-")).grid(row = 3,column=3)
Button(root,text = "*",command=lambda:get_operation("*")).grid(row = 4,column=3)
Button(root,text = "/",command=lambda:get_operation("/")).grid(row = 5,column=3)

#more operations
Button(root,text = "pi",command=lambda:get_operation("*3.14")).grid(row = 2,column=4)
Button(root,text = "%",command=lambda:get_operation("%")).grid(row = 3,column=4)
Button(root,text = "(",command=lambda:get_operation("(")).grid(row = 4,column=4)
Button(root,text = "exp",command=lambda:get_operation("**")).grid(row = 5,column=4)

Button(root,text = "<-",command=lambda: undo()).grid(row = 2,column=5)
Button(root,text = "x!",).grid(row = 3,column=5)
Button(root,text = ")",command=lambda:get_operation(")")).grid(row = 4,column=5)
Button(root,text = "^2",command=lambda:get_operation("**2")).grid(row = 5,column=5)

root.mainloop()



