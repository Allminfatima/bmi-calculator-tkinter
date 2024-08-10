import tkinter as tk
from tkinter import messagebox

# Function to validate that input is a number
def validate_number_input(value):
    if value == "" or value.replace('.', '', 1).isdigit():
        return True
    else:
        return False

# Function to calculate BMI and display the result
def calculate_bmi():
    try:
        # Retrieve user input
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        # Validate the input
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive values.")

        # Calculate BMI
        bmi = weight / (height * height)
        bmi = round(bmi, 2)  # Round to 2 decimal places

        # Determine BMI category
        if bmi <= 16:
            category = 'severely underweight :('
        elif bmi <= 18.5:
            category = 'underweight :('
        elif bmi <= 25:
            category = 'healthy :)'
        elif bmi <= 30:
            category = 'overweight :('
        else:
            category = 'suffering from obesity.'

        # Display the result
        result_label.config(text=f'Your BMI is: {bmi}\nYou are {category}')

    except ValueError as e:
        messagebox.showerror("Invalid input", f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Load and display the logo
logo_img = tk.PhotoImage(file="download.png")  # Replace with the path to your logo file
logo_label = tk.Label(root, image=logo_img)
logo_label.pack(side="left", padx=10, pady=10)

# Create a validation command for numeric input
validate_cmd = root.register(validate_number_input)

# Create and place the widgets
tk.Label(root, text="Enter your height (in meters):").pack(pady=5)
height_entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, '%P'))
height_entry.pack(pady=5)

tk.Label(root, text="Enter your weight (in kilograms):").pack(pady=5)
weight_entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, '%P'))
weight_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
