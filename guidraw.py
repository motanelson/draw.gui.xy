import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class RectDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor e Desenhador CSV")
        self.root.geometry("800x600")
        self.root.configure(bg="yellow")

        # Menus
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Run", command=self.run)
        menu_bar.add_cascade(label="Menu", menu=file_menu)
        self.root.config(menu=menu_bar)

        # Caixa de Texto
        self.text = tk.Text(self.root, width=25, bg="yellow", fg="black")
        self.text.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Área de Desenho
        self.canvas = tk.Canvas(self.root, bg="yellow", width=600, height=600)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                with open(filepath, newline='') as f:
                    reader = csv.reader(f)
                    self.text.delete("1.0", tk.END)
                    for row in reader:
                        self.text.insert(tk.END, ",".join(row) + "\n")
            except Exception as e:
                messagebox.showerror("Erro ao abrir", str(e))

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                with open(filepath, 'w', newline='') as f:
                    writer = csv.writer(f)
                    lines = self.text.get("1.0", tk.END).strip().splitlines()
                    for line in lines:
                        parts = [s.strip() for s in line.split(',')]
                        if len(parts) == 4:
                            writer.writerow(parts)
            except Exception as e:
                messagebox.showerror("Erro ao gravar", str(e))

    def run(self):
        # Limpa e pinta de amarelo
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 600, 600, fill="yellow", outline="yellow")

        # Grid
        grid_color = "#CCCC00"  # amarelo escuro visível
        for i in range(0, 600, 20):
            self.canvas.create_line(i, 0, i, 600, fill=grid_color)
            self.canvas.create_line(0, i, 600, i, fill=grid_color)

        # Desenhar retângulos
        lines = self.text.get("1.0", tk.END).strip().splitlines()
        for line in lines:
            try:
                x, y, w, h = map(int, line.strip().split(','))
                self.canvas.create_rectangle(x, y, x + w, y + h, fill="black")
            except:
                continue  # ignora linhas inválidas

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = RectDrawerApp(root)
    root.mainloop()

