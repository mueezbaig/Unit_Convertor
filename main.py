import tkinter as tk
from tkinter import ttk

def choose_length_conversion():
    length_frame.grid(row=2, column=0)
    area_frame.grid_forget()

def choose_area_conversion():
    area_frame.grid(row=2, column=0)
    length_frame.grid_forget()

def convert_length():
    length_value = length_entry.get()
    if not length_value:
        result_label.config(text="Please enter a length value.", foreground="red")
        return
    
    length_value = float(length_value)
    
    if length_choice.get() == 1:
        
        result = length_value / 30.48
        result_label.config(text=f"{length_value} cm is equal to {result:.5f} feet.", foreground="black")

    elif length_choice.get() == 2:
        
        result = length_value * 12
        result_label.config(text=f"{length_value} feet is equal to {result:.2f} inches.", foreground="black")

def convert_area():
    area_value = area_entry.get()
    if not area_value:
        result_label.config(text="Please enter an area value.", foreground="red")
        return
    
    area_value = float(area_value)
    
    if area_choice.get() == 1:
        
        result = area_value * 0.092903
        result_label.config(text=f"{area_value} sqft is equal to {result:.6f} sqm.", foreground="black")
    elif area_choice.get() == 2:
        
        result = area_value / 107600
        result_label.config(text=f"{area_value} sqft is equal to {result:.7f} hectares.", foreground="black")
    elif area_choice.get() == 3:
        
        result = area_value / 43560
        result_label.config(text=f"{area_value} sqft is equal to {result:.6f} acres.", foreground="black")


root = tk.Tk()
root.title("Unit Converter")


choose_conversion_frame = ttk.Frame(root, padding=20)
choose_conversion_frame.grid(row=0, column=0, padx=20, pady=20)

ttk.Label(choose_conversion_frame, text="Choose Type of Conversion:", font=('Helvetica', 14)).grid(row=0, column=0, columnspan=2, sticky="w")

ttk.Button(choose_conversion_frame, text="Length", command=choose_length_conversion).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(choose_conversion_frame, text="Area", command=choose_area_conversion).grid(row=1, column=1, padx=10, pady=5)


length_frame = ttk.Frame(root, padding=20)

ttk.Label(length_frame, text="Enter Length Value:", font=('Helvetica', 14)).grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(length_frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

length_choice = tk.IntVar()
length_choice.set(1) 

length_dict = {
    1: "Centimeter to Feet",
    2: "Feet to Inches"
}

for key, value in length_dict.items():
    ttk.Radiobutton(length_frame, text=value, variable=length_choice, value=key).grid(row=key+1, column=0, columnspan=2, sticky="w")

ttk.Button(length_frame, text="Convert", command=convert_length).grid(row=4, column=0, columnspan=2, pady=10)


area_frame = ttk.Frame(root, padding=20)

ttk.Label(area_frame, text="Enter Area Value:", font=('Helvetica', 14)).grid(row=0, column=0, padx=5, pady=5)
area_entry = ttk.Entry(area_frame)
area_entry.grid(row=0, column=1, padx=5, pady=5)

area_choice = tk.IntVar()
area_choice.set(1)  

area_dict = {
    1: "Square Feet to Square Meters",
    2: "Square Feet to Hectares",
    3: "Square Feet to Acres"
}

for key, value in area_dict.items():
    ttk.Radiobutton(area_frame, text=value, variable=area_choice, value=key).grid(row=key+1, column=0, columnspan=2, sticky="w")

ttk.Button(area_frame, text="Convert", command=convert_area).grid(row=5, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="", font=('Helvetica', 14))
result_label.grid(row=3, column=0, pady=20)

root.mainloop()
