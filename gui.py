import tkinter as tk
from tkinter import messagebox
import json
import os

def submit_action():
    # Get the input from text fields
    name = entry_name.get()
    eyc_no = entry_eyc_no.get()
    aadhar_no = entry_aadhar_no.get()
    address = entry_address.get()
    email = entry_email.get()
    no_of_units = entry_no_of_units.get()

    # Prepare the data to be saved
    user_data = {
        "name": name,
        "eyc_no": eyc_no,
        "aadhar_no": aadhar_no,
        "address": address,
        "email": email,
        "no_of_units": no_of_units
    }

    # Load existing data from the JSON file if it exists
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Append the new user data
    data.append(user_data)

    # Write the updated data back to the JSON file
    with open('demo.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Show a message box with the input name
    if name:
        messagebox.showinfo("Submission", f"Hello, {name}!\nData has been saved.")
    else:
        messagebox.showwarning("Warning", "Please enter your name.")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("GUI for Users")

    # Set the size of the window
    root.geometry("400x300")

    # Create Labels
    global entry_name, entry_eyc_no, entry_aadhar_no, entry_address, entry_email, entry_no_of_units  # Global to access inside submit_action function
    label_name = tk.Label(root, text="Enter your name:")
    label_eyc_no = tk.Label(root, text="Enter your EYC no.:")
    label_aadhar_no = tk.Label(root, text="Enter your Aadhaar no.:")
    label_address = tk.Label(root, text="Enter your address:")
    label_email = tk.Label(root, text="Enter your email:")
    label_no_of_units = tk.Label(root, text="Enter no. of units:")

    # Create Text Fields (Entry widgets)
    entry_name = tk.Entry(root, width=30)
    entry_eyc_no = tk.Entry(root, width=30)
    entry_aadhar_no = tk.Entry(root, width=30)
    entry_address = tk.Entry(root, width=30)
    entry_email = tk.Entry(root, width=30)
    entry_no_of_units = tk.Entry(root, width=30)

    # Create a Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit_action)

    # Place the components on the window using the grid layout
    label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_eyc_no.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_eyc_no.grid(row=1, column=1, padx=10, pady=10)

    label_aadhar_no.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_aadhar_no.grid(row=2, column=1, padx=10, pady=10)

    label_address.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_address.grid(row=3, column=1, padx=10, pady=10)

    label_email.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_email.grid(row=4, column=1, padx=10, pady=10)

    label_no_of_units.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    entry_no_of_units.grid(row=5, column=1, padx=10, pady=10)

    submit_button.grid(row=6, columnspan=2, pady=20)

    # Start the GUI main loop
    root.mainloop()

if __name__ == "__main__":
    main()
