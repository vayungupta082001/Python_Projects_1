import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.input_string = ""

        # Create screen label
        self.screen = tk.Label(master, text="0", width=20, font=("Arial", 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 12),
                           command=lambda: self.update_input(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def update_input(self, text):
        if text == "C":
            self.input_string = ""
        elif text == "=":
            self.evaluate()
        else:
            self.input_string += text

        self.screen.config(text=self.input_string)

    def evaluate(self):
        try:
            result = eval(self.input_string)
            self.screen.config(text=result)
            self.input_string = str(result)
        except:
            self.screen.config(text="Error")
            self.input_string = ""

# Create the main window
root = tk.Tk()
app = Calculator(root)

# Set the dimensions of the window
root.geometry("200x344")

# Start the mainloop to display the window
root.mainloop()
