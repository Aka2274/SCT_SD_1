import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_scale = combo_from.get()
        to_scale = combo_to.get()

        if from_scale == to_scale:
            result_var.set(f"{temp:.2f} {scale_symbols[to_scale]}")
            return

        # Convert to Celsius
        if from_scale == "Celsius":
            celsius = temp
        elif from_scale == "Fahrenheit":
            celsius = (temp - 32) * 5 / 9
        elif from_scale == "Kelvin":
            celsius = temp - 273.15

        # Convert from Celsius to target
        if to_scale == "Celsius":
            converted = celsius
        elif to_scale == "Fahrenheit":
            converted = (celsius * 9 / 5) + 32
        elif to_scale == "Kelvin":
            converted = celsius + 273.15

        result_var.set(f"{converted:.2f} {scale_symbols[to_scale]}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

scale_symbols = {
    "Celsius": "°C",
    "Fahrenheit": "°F",
    "Kelvin": "K"
}

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#E6E6FA")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 12), background="#E6E6FA", foreground="#000080")
style.configure("TButton", font=("Segoe UI", 12), background="#87CEEB", foreground="black")
style.configure("TEntry", fieldbackground="#FFFFFF", foreground="black", font=("Segoe UI", 12))
style.configure("TCombobox", font=("Segoe UI", 12))

# Title
title_label = tk.Label(root, text="Temperature Converter", font=("Segoe UI", 16, "bold"), bg="#E6E6FA", fg="#000080")
title_label.pack(pady=15)

# Entry for temperature
ttk.Label(root, text="Enter Temperature:").pack(pady=8)
entry_temp = ttk.Entry(root, font=("Segoe UI", 12), width=20)
entry_temp.pack(pady=8)

# Frame for dropdowns
dropdown_frame = tk.Frame(root, bg="#E6E6FA")
dropdown_frame.pack(pady=10)

# "From" dropdown
ttk.Label(dropdown_frame, text="From:").grid(row=0, column=0, padx=5)
combo_from = ttk.Combobox(dropdown_frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Segoe UI", 12), width=15)
combo_from.current(0)
combo_from.grid(row=0, column=1, padx=10)

# "To" dropdown
ttk.Label(dropdown_frame, text="To:").grid(row=0, column=2, padx=5)
combo_to = ttk.Combobox(dropdown_frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Segoe UI", 12), width=15)
combo_to.current(1)
combo_to.grid(row=0, column=3, padx=10)

# Convert button
ttk.Button(root, text="Convert", command=convert_temperature).pack(pady=15)

# Output frame
output_frame = tk.Frame(root, bg="#FFF8DC", bd=1, relief="solid")
output_frame.pack(pady=10, ipadx=40, ipady=3)

result_var = tk.StringVar()
result_label = tk.Label(output_frame, textvariable=result_var, font=("Segoe UI", 14, "bold"), bg="#FFF8DC", fg="darkred")
result_label.pack()

root.mainloop()
