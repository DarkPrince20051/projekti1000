import tkinter as tk
from tkinter import messagebox

class DrawRectangleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Crtanje pravokutnika")

        # Postavljanje početnih vrijednosti
        self.start_x = tk.StringVar(value="0")
        self.start_y = tk.StringVar(value="0")
        self.side_a = tk.DoubleVar(value=0.0)
        self.side_b = tk.DoubleVar(value=0.0)

        # Grafički elementi
        self.label_start = tk.Label(master, text="Početna točka (x, y):")
        self.entry_start_x = tk.Entry(master, textvariable=self.start_x)
        self.entry_start_y = tk.Entry(master, textvariable=self.start_y)

        self.label_a = tk.Label(master, text="Duljina stranice a:")
        self.entry_a = tk.Entry(master, textvariable=self.side_a)

        self.label_b = tk.Label(master, text="Duljina stranice b:")
        self.entry_b = tk.Entry(master, textvariable=self.side_b)

        self.button_draw = tk.Button(master, text="Crtaj pravokutnik", command=self.draw_rectangle)
        self.button_reset = tk.Button(master, text="Resetiraj", command=self.reset_values)
        self.button_close = tk.Button(master, text="Zatvori", command=self.close_window)

        # Razmještaj grafičkih elemenata
        self.label_start.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_start_x.grid(row=0, column=1, padx=5, pady=5)
        self.entry_start_y.grid(row=0, column=2, padx=10, pady=5)

        self.label_a.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_a.grid(row=1, column=1, padx=5, pady=5)

        self.label_b.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_b.grid(row=2, column=1, padx=5, pady=5)

        self.button_draw.grid(row=3, column=0, pady=10)
        self.button_reset.grid(row=3, column=1, pady=10)
        self.button_close.grid(row=3, column=2, pady=10)

        # Platno za crtanje
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.grid(row=0, column=3, rowspan=4, padx=10, pady=10)

    def draw_rectangle(self):
        try:
            start_x = int(self.start_x.get())
            start_y = int(self.start_y.get())
            side_a = float(self.side_a.get())
            side_b = float(self.side_b.get())

            # Izračun krajnjih točaka pravokutnika
            end_x = start_x + side_a
            end_y = start_y + side_b

            # Brišemo prethodno nacrtan pravokutnik
            self.canvas.delete("rectangle")

            # Crtamo novi pravokutnik
            self.canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="red", outline="blue", tags="rectangle")

        except ValueError:
            messagebox.showerror("Greška", "Unesite valjane brojeve za točke i duljine stranica.")

    def reset_values(self):
        self.start_x.set("0")
        self.start_y.set("0")
        self.side_a.set(0.0)
        self.side_b.set(0.0)
        self.canvas.delete("rectangle")
        self.entry_start_x.focus_set()

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawRectangleApp(root)
    root.mainloop()
