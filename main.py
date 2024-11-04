from tkinter import *

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


root.title("Calculator") # Set the title of the window
root.minsize(width=230, height=150)
root.config(padx=10, pady=10) # Add padding around the window edges

# Create the display area for calculations and results
display = Entry(root, width=15, font=("Arial", 18), borderwidth=2,
                relief="solid", justify='right')
display.grid(row=0, column=0, columnspan=6, pady=(10, 10), sticky="EW") # Position the display

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
# Create buttons for numbers 1-9 in a 3x3 grid
for x in range(3):
    for y in range(3):
        # Create a button for each number
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=2, height=2, highlightthickness=0,
                        command=lambda text=button_text: get_number(text))
        button.grid(row=x + 2, column=y)  # Position the button in the grid
        counter += 1

# Create the button for number 0 and place it below the 1-9 buttons
zero_button = Button(root, text=0, width=2, height=2, highlightthickness=0,
                     command=lambda text=0: get_number(text))
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
                            command=lambda text=button_text: get_operation(text))
            count += 1
            button.grid(row=x + 2, column=y + 3)  # Position the operation button

# Run the application
root.mainloop()
