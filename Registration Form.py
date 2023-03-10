import tkinter as tk

# Create main window
root = tk.Tk()
root.geometry("270x125")
root.title("Registration Form")

# Define pop-up window function
def registration_details(name, email, phone):
    # Create new Toplevel window
    popup = tk.Toplevel()
    popup.geometry("270x150")
    
    # Add labels and entry widgets to display details
    tk.Label(popup, text="Name:").grid(row=0, column=0)
    tk.Label(popup, text=name).grid(row=0, column=1)
    
    tk.Label(popup, text="Email:").grid(row=1, column=0)
    tk.Label(popup, text=email).grid(row=1, column=1)
    
    tk.Label(popup, text="Phone Number:").grid(row=2, column=0)
    tk.Label(popup, text=phone).grid(row=2, column=1)
    
    # Add button to close pop-up window
    tk.Button(popup, text="Close", command=popup.destroy).grid(row=3, column=1)

# Define function to get input from user
def submit_registration():
    # Get input from user
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
    # Call pop-up window function with details
    registration_details(name, email, phone)

# Create labels and entry widgets for registration form
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Phone Number:").grid(row=2, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

# Create button to submit registration
tk.Button(root, text="Submit", command=submit_registration).grid(row=3, column=1)

# Run the main loop
root.mainloop()
