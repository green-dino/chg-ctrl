import tkinter as tk
from tkinter import ttk

def on_dropdown_change(event):
    selected_option = dropdown_var.get()
    feedback_label.config(text=f"Selected Option: {selected_option}")

    if selected_option in options_mapping:
        show_second_dropdown()
    else:
        hide_second_dropdown()

    update_second_options(selected_option)

def show_second_dropdown():
    second_dropdown.grid(row=1, column=0, padx=10, pady=10)

def hide_second_dropdown():
    second_dropdown.grid_forget()

def update_second_options(selected_option):
    second_options = options_mapping.get(selected_option, [])
    second_dropdown['values'] = second_options

# Dictionary to map first drop-down options to corresponding second drop-down options
options_mapping = {
    "Find": ["1", "2", "3"],
    "Fix": ["A", "B", "C"],
    "Finish": ["X", "Y", "Z"],
    "Exploit": ["!", "@", "#"],
    "Analyze": ["Red", "Green", "Blue"],
    "Disseminate": ["Alpha", "Beta", "Gamma"],
}

# Create the main application window
root = tk.Tk()
root.title("Select an Option")

# Create a variable to hold the selected option for the first drop-down
dropdown_var = tk.StringVar(root)

# Create a drop-down menu and set the initial value to the first option in the dictionary
options = list(options_mapping.keys())  # Extract option labels from the dictionary
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options)
dropdown.current(0)
dropdown.grid(row=0, column=0, padx=10, pady=10)

# Bind the first drop-down to the on_dropdown_change function
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# Create a variable to hold the selected option for the second drop-down
second_dropdown_var = tk.StringVar(root)

# Create the second drop-down menu, but hide it initially
second_dropdown = ttk.Combobox(root, textvariable=second_dropdown_var)
second_dropdown.grid_forget()

# Create a label for user feedback
feedback_label = tk.Label(root, text="", padx=10, pady=10)
feedback_label.grid(row=2, column=0)

# Start the main event loop
root.mainloop()
