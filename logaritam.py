import tkinter as tk
from math import log10
from tkinter import messagebox

def izracunaj_logaritam():
    try:
        baza = float(entry_baza.get())
        broj = float(entry_broj.get())

        rezultat = log10(broj) / log10(baza)

        rezultat_label.config(text=f"Rezultat: {rezultat:.4f}")
    except ValueError:
        rezultat_label.config(text="Unesite valjane brojeve!")

def resetiraj_unose():
    entry_baza.delete(0, tk.END)
    entry_broj.delete(0, tk.END)
    rezultat_label.config(text="Rezultat: ")
    entry_baza.focus_set()

def izlaz():
    odgovor = messagebox.askyesno("Izlaz", "Želite li zatvoriti program?")
    if odgovor:
        root.destroy()

# Glavni prozor
root = tk.Tk()
root.title("Logaritam Kalkulator")
root.geometry("400x300")
root.resizable(False,False)

# Unos baze logaritma
label_baza = tk.Label(root, text="Unesite bazu logaritma:")
label_baza.pack()

entry_baza = tk.Entry(root)
entry_baza.pack()

# Unos broja
label_broj = tk.Label(root, text="Unesite broj:")
label_broj.pack()

entry_broj = tk.Entry(root)
entry_broj.pack()

# Gumb za izračunavanje logaritma
izracunaj_gumb = tk.Button(root, text="Izračunaj", command=izracunaj_logaritam)
izracunaj_gumb.pack(pady=5)  # Dodajemo razmak (5 piksela) ispod gumba

# Rezultat
rezultat_label = tk.Label(root, text="Rezultat: ")
rezultat_label.pack()

# Gumb za resetiranje unosa
reset_gumb = tk.Button(root, text="Resetiraj", command=resetiraj_unose)
reset_gumb.pack(pady=5)  # Dodajemo razmak (5 piksela) ispod gumba

# Gumb za izlaz s pitanjem
izlaz_gumb = tk.Button(root, text="Izlaz", command=izlaz)
izlaz_gumb.pack(pady=5)

root.mainloop()
