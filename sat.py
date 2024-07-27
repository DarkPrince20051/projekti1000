import tkinter as tk
from time import strftime
from tkinter import messagebox

def vreme():
    s = strftime('%H:%M:%S %p')
    label.config(text=s)
    label.after(1000, vreme)

def exit_aplication():
    response = messagebox.askquestion("Exit", "Do you really want to exit?")
    if response.lower() == 'yes':
        root.destroy()


root = tk.Tk()
root.title("Sat")
root.geometry("400x300")

label = tk.Label(root, font=('calibri', 40, 'bold'), foreground='blue', background='white')
label.pack(pady=(root.winfo_reqheight()-40)//2)

gumb_zatvori = tk.Button(root, text="Exit", command=exit_aplication)
gumb_zatvori.pack(pady=10)

vreme()
root.mainloop()
