from tkinter import *

# Create a calculator class
class Calculator:
    def __init__(self, master):
        """
        Method that initializes the object's attributes
        """

        # Assign reference to the main window of the application
        self.master = master

        # Add a name to our application
        master.title("Python Calculator")

        # Get the screen width and height
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set the window size to 90% of the screen dimensions
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        master.geometry(f"{window_width}x{window_height}")

        # Set the background color of the main window
        master.configure(bg='#c2f0f0')

        # Create a line where we display the equation
        self.equation = Entry(master, font=('Arial', 24), borderwidth=5, relief=RIDGE)
        
        # Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Execute the .createButton() method
        self.createButton()

        # Configure grid layout to expand widgets
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def createButton(self):
        """
        Method to create a button

        INPUT: nothing
        OUTPUT: creates a button
        """

        # We first create each button one by one with the value we want
        # Using addButton() method which is described below
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton("+")
        b_sub = self.addButton("-")
        b_mult = self.addButton("*")
        b_div = self.addButton("/")
        b_clear = self.addButton("c")
        b_equal = self.addButton("=")

        # Arrange the buttons into lists which represent calculator rows
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mult]
        row4 = [b_clear, b0, b_equal, b_div]

        # Assign each button to a particular location on the GUI
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for buttn in row:
                buttn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
                c += 1
            r += 1

    def addButton(self, value):
        """
        Method to process the creation of a button and make it clickable

        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: returns a designed button object
        """

        return Button(
            self.master,
            text=value,
            font=('Arial', 18),
            command=lambda: self.clickButton(str(value)),
            relief=RAISED,
            borderwidth=3,
            bg='#add8e6',  # Set background color of buttons
            activebackground='#87cefa',  # Set background color when button is pressed
        )

    def clickButton(self, value):
        """
        Method to add actions for button clicks

        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        """

        # Get the equation that's entered by the user
        current_equation = str(self.equation.get())

        # If user clicked "c", then clear the screen
        if value == "c":
            self.equation.delete(0, END)

        # If user clicked "=", then compute the answer and display it
        elif value == "=":
            try:
                answer = str(eval(current_equation))
                self.equation.delete(0, END)
                self.equation.insert(0, answer)
            except:
                self.equation.delete(0, END)
                self.equation.insert(0, "Error")

        # If user clicked any other button, then add it to the equation line
        else:
            self.equation.insert(END, value)

# Execution
if __name__ == "__main__":
    # Create the main window of an application
    root = Tk()

    # Tell our calculator class to use this window
    my_gui = Calculator(root)

    # Executable loop for the application, waits for user input
    root.mainloop()
