import tkinter as tk

def convert_to_cm():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Create and place widgets
tk.Label(root, text="Enter length in inches:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=2, pady=10)

tk.Button(root, text="Convert", command=convert_to_cm).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
