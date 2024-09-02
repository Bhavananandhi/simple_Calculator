import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600+0+0")

# Create the display where numbers and results will appear
display = tk.Entry(root, background="Lightblue",font=("Arial", 20), bd=10 ,insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0,columnspan=3)

# Define the button click function (for numbers)
def button_click(number):
    current = display.get()  # Get the current number in the display
    display.delete(0, tk.END)  # Clear the display
    display.insert(0, current + str(number))  # Insert the new number

# Define the function for the "+" button
def button_add():
    first_number = display.get()  # Get the first number
    global f_num  # Make it accessible globally
    global math  # Store the operation type
    math = "addition"
    f_num = float(first_number)  # Convert the number to a float
    display.delete(0, tk.END)  # Clear the display

# Define the function for the "-" button
def button_subtract():
    first_number = display.get()  # Get the first number
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Define the function for the "*" button
def button_multiply():
    first_number = display.get()  # Get the first number
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Define the function for the "/" button
def button_divide():
    first_number = display.get()  # Get the first number
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)

# Define the function for the "=" button
def button_equal():
    second_number = display.get()  # Get the second number
    display.delete(0, tk.END)  # Clear the display

    if math == "addition":
        display.insert(0, f_num + float(second_number))  # Perform addition and show the result
    elif math == "subtraction":
        display.insert(0, f_num - float(second_number))  # Perform subtraction and show the result
    elif math == "multiplication":
        display.insert(0, f_num * float(second_number))  # Perform multiplication and show the result
    elif math == "division":
        display.insert(0, f_num / float(second_number))  # Perform division and show the result

# Define the clear button function
def button_clear():
    display.delete(0, tk.END)  # Clear the display

# Create buttons for numbers 0-9
button_1 = tk.Button(root, text="1", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, font=("Arial", 18), command=lambda: button_click(0))

# Create buttons for operations (+, -, *, /, =, Clear)
button_add = tk.Button(root, text="+", padx=20, pady=20, font=("Arial", 18), command=button_add)
button_subtract = tk.Button(root, text="-", padx=20, pady=20, font=("Arial", 18), command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=20, pady=20, font=("Arial", 18), command=button_multiply)
button_divide = tk.Button(root, text="/", padx=20, pady=20, font=("Arial", 18), command=button_divide)
button_equal = tk.Button(root, text="=", padx=20, pady=20, font=("Arial", 18), command=button_equal)
button_clear = tk.Button(root,background="yellow" ,text="Clear", padx=20, pady=20, font=("Arial", 18), command=button_clear)

# Place the number buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

# Place the operation buttons on the grid
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)
button_equal.grid(row=5, column=0)
button_clear.grid(row=4, column=3)

# Keep the window open and running
root.mainloop()