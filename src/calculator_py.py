import tkinter as tk
from tkinter import messagebox
import math

# Calculator functions
def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        show_error()

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        show_error()

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        show_error()

def divide():
    try:
        y = float(entry2.get())
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        result.set(float(entry1.get()) / y)
    except ValueError as e:
        show_error(str(e))

def power():
    try:
        result.set(float(entry1.get()) ** float(entry2.get()))
    except ValueError:
        show_error()

def square_root():
    try:
        x = float(entry1.get())
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        result.set(math.sqrt(x))
    except ValueError as e:
        show_error(str(e))

def percentage():
    try:
        total = float(entry2.get())
        if total == 0:
            raise ValueError("Total cannot be zero.")
        result.set((float(entry1.get()) / total) * 100)
    except ValueError as e:
        show_error(str(e))

def show_error(msg="Please enter valid numbers."):
    messagebox.showerror("Error", msg)

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields
tk.Label(root, text="First Number / Value:").grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number / Total:").grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Result display
result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=2, column=0, sticky="w")
tk.Label(root, textvariable=result).grid(row=2, column=1, sticky="w")

# Buttons
tk.Button(root, text="Add", command=add).grid(row=3, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=3, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=4, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=4, column=1)
tk.Button(root, text="Power", command=power).grid(row=5, column=0)
tk.Button(root, text="Square Root", command=square_root).grid(row=5, column=1)
tk.Button(root, text="Percentage", command=percentage).grid(row=6, column=0)

# Run the application
root.mainloop()
