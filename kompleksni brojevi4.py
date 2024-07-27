import tkinter as tk
from tkinter import messagebox
import cmath

def calculate():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        complex_number = complex(x, y)

        # Prikaz rezultata
        argument_radians = cmath.phase(complex_number)
        argument_degrees = argument_radians * (180 / cmath.pi)

        # Dodaj 360 stupnjeva za negativne kutove
        if argument_degrees < 0:
            argument_degrees += 360

        var_result.set(f"Argument: {argument_degrees}°\n"
                       f"Konjugacija: {complex_number.conjugate()}\n"
                       f"Realni dio: {complex_number.real}\n"
                       f"Imaginarni dio: {complex_number.imag}\n"
                       f"Apsolutna vrijednost: {abs(complex_number)}")
    except ValueError:
        messagebox.showerror("Greška", "Unesite ispravne brojeve za x i y.")

def reset():
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    var_result.set("")
    entry_x.focus_set()

def close_window():
    root.destroy()

# Glavni prozor
root = tk.Tk()
root.title("Kalkulator kompleksnih brojeva")
root.geometry("400x350")
root.resizable(False,False)

# Unos za x
label_x = tk.Label(root, text="Realni dio (x):")
label_x.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=5)

# Unos za y
label_y = tk.Label(root, text="Imaginarni dio (y):")
label_y.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1, padx=10, pady=5)

# Gumbi
button_calculate = tk.Button(root, text="Izračunaj", command=calculate)
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)

button_reset = tk.Button(root, text="Resetiraj", command=reset)
button_reset.grid(row=3, column=0, columnspan=2, pady=5)

button_close = tk.Button(root, text="Zatvori", command=close_window)
button_close.grid(row=4, column=0, columnspan=2, pady=5)

# Rezultat
var_result = tk.StringVar()
label_result = tk.Label(root, textvariable=var_result)
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
