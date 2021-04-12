import tkinter
import threading
import time

# Declaring and initializing a tkinter frame
root = tkinter.Tk()
# Adding a title to the frame
root.title("Calculator")
# Setting the frame as non resizable
root.resizable(0, 0)
# Setting the frame's dimensions
root.geometry("230x300")
# Setting the frame's background color
root.configure(bg="black")
# Declaring variable expression as empty string
expression = ""

# Functions
def add(value):
    global expression
    # Adding the value received from user input to the expression
    expression += value
    # Displaying the expression (result) on the result label
    label_result.config(text=expression)

def clear():
    global expression
    # Setting the expression variable to an empty string
    expression = ""
    # Displaying the expression (null) on the result label
    label_result.config(text=expression)

def calculate():
    global expression
    # Declaring result as an empty string
    result = ""
    # If the expression is not null, pass expression to the built in eval() function to
    # parse the string as a python expression
    if expression != "":
        try:
            result = eval(expression)
        # If the expression is invalid, display an error and reset the expression variable to
        # an empty string
        except:
            result = "error"
            expression = ""
    # Displaying the result on the result label
    label_result.config(text=result)
    expression = str(result)

# Handling keyboard input, converting key strokes to the corresponding value and passin it to
# the add() function
def key_handler(event):
    global expression
    if event.keysym in ("1","2","3","4","5","6","7","8","9","0"):
        add(event.keysym)
    elif event.keysym =="period":
        add(".")
    elif event.keysym == "plus":
        add("+")
    elif event.keysym == "minus":
        add("-")
    elif event.keysym == "asterisk":
        add("*")
    elif event.keysym == "slash":
        add("/")
    elif event.keysym in ("c","C"):
        clear()
    # Starting a thread once the user hits return or equal
    elif event.keysym in ("Return","equal"):
        threading.Thread(target=calculate).start()
    # Deleting the last value in the expression
    elif event.keysym == "BackSpace":
        expression = expression[0:len(expression)-1]
        label_result.config(text=expression)

root.bind("<Key>", key_handler)

# Creating the GUI
#
label_result = tkinter.Label(root, text="0", bg="black", fg="white", font=('Helvetica', '20'))
label_result.grid(row=0, column=0, columnspan=4)
# Displaying numbers
#
button_1 = tkinter.Button(root, text="1", command=lambda: add("1"), height="3", width="6", font=('Helvetica', '15'))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"), height="3", width="6", font=('Helvetica', '15'))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"), height="3", width="6", font=('Helvetica', '15'))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/",command=lambda: add("/"), height="3", width="6", font=('Helvetica', '15'))
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4", command=lambda: add("4"), height="3", width="6", font=('Helvetica', '15'))
button_4.grid(row=3, column=0)

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"), height="3", width="6", font=('Helvetica', '15'))
button_5.grid(row=3, column=1)

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"), height="3", width="6", font=('Helvetica', '15'))
button_6.grid(row=3, column=2)
# Arithmetic sign (multiplication)
#
button_multiply = tkinter.Button(root, text="*", command=lambda: add("*"), height="3", width="6", font=('Helvetica', '15'))
button_multiply.grid(row=3, column=3)

button_7 = tkinter.Button(root, text="7", command=lambda: add("7"), height="3", width="6", font=('Helvetica', '15'))
button_7.grid(row=4, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"), height="3", width="6", font=('Helvetica', '15'))
button_8.grid(row=4, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"), height="3", width="6", font=('Helvetica', '15'))
button_9.grid(row=4, column=2)
# Arithmetic sign (addition)
#
button_add = tkinter.Button(root, text="+", command=lambda: add("+"), height="3", width="6", font=('Helvetica', '15'))
button_add.grid(row=4, column=3)

button_clear = tkinter.Button(root, text="C", command=lambda: clear(), height="3", width="6", font=('Helvetica', '15'))
button_clear.grid(row=5, column=0)

button_0 = tkinter.Button(root, text="0", command=lambda: add("0"), height="3", width="6", font=('Helvetica', '15'))
button_0.grid(row=5, column=1)
# Arithemtic sign (dot)
#
button_dot = tkinter.Button(root, text=".", command=lambda: add("."), height="3", width="6", font=('Helvetica', '15'))
button_dot.grid(row=5, column=2)
# Arithmetic sign (subtraction)
#
button_subtract = tkinter.Button(root, text="-", command=lambda: add("-"), height="3", width="6", font=('Helvetica', '15'))
button_subtract.grid(row=5, column=3)
# Arithmetic sign (equal to)
#
button_equals = tkinter.Button(root, text="=", command=lambda: threading.Thread(target=calculate).start(), height="3", width="26", font=('Helvetica', '15'))
button_equals.grid(row=6, column=0, columnspan=4)

root.mainloop()
