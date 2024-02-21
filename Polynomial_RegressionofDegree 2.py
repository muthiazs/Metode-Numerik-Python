import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Fungsi untuk menghitung koefisien regresi polinomial derajat 2
def calculate_coefficients(x, y):
    coefficients = np.polyfit(x, y, 2)
    return coefficients

# Fungsi untuk membuat grafik
def create_plot(x, y, coefficients):
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(x, y, color='red')
    x_model = np.linspace(min(x), max(x), 100)
    y_model = sum(coefficients[i]*x_model**(2-i) for i in range(len(coefficients)))
    ax.plot(x_model, y_model, color='blue')
    return fig

# Fungsi untuk menangani klik tombol
def on_button_click():
    x = list(map(float, entry_x.get().split(',')))
    y = list(map(float, entry_y.get().split(',')))
    coefficients = calculate_coefficients(x, y)
    fig = create_plot(x, y, coefficients)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_result = tk.Label(root, text=f"Koefisien: {coefficients}")
    label_result.pack()
    label_equation = tk.Label(root, text=f"Persamaan: y = {coefficients[0]}x² + {coefficients[1]}x + {coefficients[2]}")
    label_equation.pack()

# Membuat antarmuka pengguna
root = tk.Tk()
root.title("Polynomial Regression Degree 2")

frame = tk.Frame(root)
frame.pack()

label_judul = tk.Label(frame, text="Polynomial Regression Degree 2", font= ("Comic n Sans", 30, "bold"), fg="maroon")
label_judul.pack()

label_anggota = tk.Label(frame, text="ANGGOTA KELOMPOK : ", font= ("Arial", 10 , "bold"), fg="Black")
label_anggota.pack()

label_nama1 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama1.pack()
label_nama2 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama2.pack()
label_nama3 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama3.pack()
label_nama4 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama4.pack()
label_nama5 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama5.pack()

label_x = tk.Label(root, text="Masukkan nilai x (pisahkan dengan koma):")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()
label_y = tk.Label(root, text="Masukkan nilai y (pisahkan dengan koma):")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()
button = tk.Button(root, text="Hitung Koefisien dan Buat Grafik", command=on_button_click)
button.pack()
root.mainloop()
