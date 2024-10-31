from tkinter import *

# Create the main application window for the calculator
root = Tk()
root.title("Calculator") # Set the title of the window
root.minsize(width=230, height=150)
root.config(padx=10, pady=10) # Add padding around the window edges

# Create the display area for calculations and results
display = Entry(root, width=15, font=("Arial", 18), borderwidth=2,
                relief="solid", justify='right')
display.grid(row=0, column=0, columnspan=6, pady=(10, 10), sticky="EW") # Position the display

counter = 1
# Create buttons for numbers 1-9 in a 3x3 grid
for x in range(3):
    for y in range(3):
        # Create a button for each number
        button = Button(root, text=counter, width=2, height=2, highlightthickness=0)
        button.grid(row=x + 2, column=y)  # Position the button in the grid
        counter += 1

# Create the button for number 0 and place it below the 1-9 buttons
zero_button = Button(root, text=0, width=2, height=2, highlightthickness=0)
zero_button.grid(row=5, column=1)

operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']

count = 0
# Loop to create buttons for each operation symbol in the list operations
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=4, height=2, highlightthickness=0)
            count += 1
            button.grid(row=x + 2, column=y + 3) # Position the operation button

# Run the application
root.mainloop()
