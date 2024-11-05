from tkinter import *
from tkinter import font
import ast

# Create the main application window for the calculator
root = Tk()
i = 0


def get_number(num):
    global i
    display.insert(index=i, string=num)
    i += 1


def get_operation(operator):
    """Function to insert an operation (e.g., "+", "-", "*", "/") into the display"""
    global i
    length = len(operator)  # Determine the length of the operator (usually 1 character)
    display.insert(index=i, string=operator)  # Insert the operator at the current cursor position
    i += length  # Move the cursor position by the length of the operator


def clear_all():
    """Clear the display by deleting all characters"""
    display.delete(0, END)


def calculate():
    """ Evaluates the mathematical expression from the display.
    Retrieves the input expression, parses it into an Abstract Syntax Tree (AST),
    compiles, and evaluates it to produce a result. If successful, clears the display
    and shows the result. If an error occurs during parsing or evaluation, it clears
    the display and displays 'Error'."""
    entire_string = display.get()  # Get the entire string input from the display
    try:
        node = ast.parse(entire_string, mode='eval')  # Parse the string into an AST node for evaluation
        result = eval(compile(node, '<string>', 'eval'))  # Compile and evaluate the AST node to get the result
        clear_all()  # Clear the display before showing the result
        display.insert(0, result)  # Insert the calculated result into the display
    except Exception:
        clear_all()
        display.insert(0, 'Error')  # Show 'Error' in the display


def undo():
    """
    Removes the last character from the string displayed in the user interface.
    This method retrieves the current string from the display. If the string is not empty,
    it removes the last character and updates the display with the new string.
    If the string is already empty, it clears the display.
    """
    entire_string = display.get()  # Get the entire string input from the display
    if len(entire_string):
        new_string = entire_string[:-1]  # Remove the last character from the string
        clear_all()
        # Insert the new string (without the last character) back into the display at index 0
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, '')  # Insert an empty string into the display

root.title("Calculator")  # Set the title of the window
root.minsize(width=300, height=200)
root.config(padx=10, pady=10)  # Add padding around the window edges

# Create the display area for calculations and results
display = Entry(root, width=20, font=("Arial", 18), borderwidth=2,
                relief="solid", justify='right')
display.grid(row=0, column=0, columnspan=6, pady=(10, 10), sticky="EW")  # Position the display

bold_font = font.Font(weight="bold")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
# Create buttons for numbers 1-9 in a 3x3 grid
for x in range(3):
    for y in range(3):
        # Create a button for each number
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=2, height=2, highlightthickness=0,
                        font=bold_font, command=lambda text=button_text: get_number(text))
        button.grid(row=x + 2, column=y)  # Position the button in the grid
        counter += 1

# Create the button for number 0 and place it below the 1-9 buttons
zero_button = Button(root, text=0, width=2, height=2, highlightthickness=0,
                     font=bold_font, command=lambda text=0: get_number(text))
zero_button.grid(row=5, column=1)

operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']

count = 0
# Loop to create buttons for each operation symbol in the list operations
for x in range(4):  # Loop over rows
    for y in range(3):  # Loop over columns
        if count < len(operations):  # Check if there are still operations to assign to buttons
            button_text = operations[count]  # Get the current operation
            # Create a button for the operation with a command to call get_operation on click
            button = Button(root, text=button_text, width=4, height=2, highlightthickness=0,
                            font=bold_font, command=lambda text=button_text: get_operation(text))
            count += 1
            button.grid(row=x + 2, column=y + 3)  # Position the operation button

# Create a button to clear the display with label 'AC' (All Clear)
Button(root, text='AC', width=2, height=2, highlightthickness=0,
       font=bold_font, command=clear_all).grid(row=5, column=0)

# Create a button to calculate the result with label '='
Button(root, text='=', width=2, height=2, highlightthickness=0,
       font=bold_font, command=calculate).grid(row=5, column=2)

# Create and configure a button widget to allow the user to undo the last action.
Button(root, text='<-', width=4, height=2, highlightthickness=0,
       font=bold_font, command=lambda: undo()).grid(row=5, column=4)

# Run the application
root.mainloop()
