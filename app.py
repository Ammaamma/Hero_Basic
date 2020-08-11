from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width = 20)
e.grid(row = 0, column = 0, columnspan = 4)

def buttonClick(number):
    e.delete(0,END)
    e.insert(0,number)


def buttonClear():
    e.delete(0,END)

def buttonAdd():
    first_number = e.get()
    global first_num
    first_num = int(first_number)
    e.delete(0,END)
    global operation
    operation = 'addition'

def buttonSubtraction():
    first_number = e.get()
    global first_num
    first_num = int(first_number)
    e.delete(0,END)
    global operation
    operation = 'subtraction'

def buttonMultiplication():
    first_number = e.get()
    global first_num
    first_num = int(first_number)
    e.delete(0,END)
    global operation
    operation = 'multiplication'

def buttonDivision():
    first_number = e.get()
    global first_num
    first_num = int(first_number)
    e.delete(0,END)
    global operation
    operation = 'division'

def buttonEqual():
    second_number = e.get()
    global second_num
    second_num = int(second_number)
    e.delete(0,END)
    if operation == 'addition':
        sum = first_num + second_num
        e.insert(0,sum)
    elif operation == 'multiplication':
        product = first_num * second_num
        e.insert(0,product)
    elif operation == 'division':
        quotient = first_num / second_num
        e.insert(0,quotient)
    elif operation == 'subtraction':
        difference = first_num - second_num
        e.insert(0,difference)

button_1=Button(root, text = 1, width = 3,command=lambda: buttonClick(1))
button_2=Button(root, text = 2, width = 3,command=lambda: buttonClick(2))
button_3=Button(root, text = 3, width = 3,command=lambda:buttonClick(3))
button_4=Button(root, text = 4, width = 3, command=lambda:buttonClick(4))
button_5=Button(root, text = 5, width = 3,command=lambda:buttonClick(5))
button_6=Button(root, text = 6, width = 3,command=lambda:buttonClick(6))
button_7=Button(root, text = 7, width = 3, command=lambda:buttonClick(7))
button_8=Button(root, text = 8, width = 3,command=lambda:buttonClick(8))
button_9=Button(root, text = 9, width = 3,command=lambda:buttonClick(9))
button_0=Button(root, text = 0, width = 3,command=lambda:buttonClick(0))

button_addition=Button(root, text = "+", width = 3, command=buttonAdd)
button_subtraction=Button(root, text = "-", width = 3,command=buttonSubtraction)
button_equal=Button(root, text = "=", width = 3,command=buttonEqual)
button_division=Button(root, text = "/", width = 3,command=buttonDivision)
button_multiplaction=Button(root, text = "*", width = 3,command=buttonMultiplication)
button_clear=Button(root, text = "c", width = 3,command=buttonClear)

button_1.grid(row =4 , column =0 )
button_2.grid(row = 4, column =1 )
button_3.grid(row = 4, column = 2)
button_4.grid(row = 3, column =0 )
button_5.grid(row = 3, column =1 )
button_6.grid(row = 3, column = 2)
button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_0.grid(row = 5, column =0)
button_multiplaction.grid(row = 4, column =4 )
button_clear.grid(row = 1, column =0 )
button_addition.grid(row = 2, column =4 )
button_subtraction.grid(row =3 , column =4 )
button_equal.grid(row =1 , column = 4)
button_division.grid(row = 5, column = 4)
root.mainloop()
