import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

root = tk.Tk()
root.title("Regresi Linier Berganda")

frame = tk.Frame(root)
frame.pack()
f1 = Frame(root, width = 900, height = 60)
f1.pack(side=TOP, pady=(16,0))

f2 = Frame(root, width = 900, height = 60)
f2.pack(side=TOP, pady=(16,0))

f3 = Frame(root, width = 900, height = 60)
f3.pack(side=TOP, pady=(16,0))

def calculate_coefficients(x,y,z):
    x = list(map(float, entry_x.get().split(',')))
    y = list(map(float, entry_y.get().split(',')))
    z = list(map(float, entry_z.get().split(',')))

    n = len(x)
    sum_x1 = sum(x)
    sum_x2 = sum(y)
    sum_y = sum(z)
    sum_x1_sq = sum(i**2 for i in x)
    sum_x2_sq = sum(i**2 for i in y)
    sum_y_sq = sum(i**2 for i in z)
    sum_x1y = sum(i*j for i, j in zip(x, z))
    sum_x2y = sum(i*j for i, j in zip(y, z))
    sum_x1x2 = sum(i*j for i,j in zip(x,y))

    sum_x1_sq_new = sum_x1_sq - ((sum_x1**2)/n)
    sum_x2_sq_new = sum_x2_sq - ((sum_x2**2)/n)
    sum_y_sq_new = sum_y_sq - ((sum_y**2)/n)
    sum_x1y_new = sum_x1y - ((sum_x1*sum_y)/n)
    sum_x2y_new = sum_x2y - ((sum_x2*sum_y)/n)
    sum_x1x2_new = sum_x1x2 - ((sum_x1*sum_x2)/n)

    b1 = ((sum_x2_sq_new*sum_x1y_new)-(sum_x1x2_new*sum_x2y_new))/((sum_x1_sq_new*sum_x2_sq_new)-(sum_x1x2_new**2))
    b2 = ((sum_x1_sq_new*sum_x2y_new)-(sum_x1x2_new*sum_x1y_new))/((sum_x1_sq_new*sum_x2_sq_new)-(sum_x1x2_new**2))
    a = (sum_y-(b1*sum_x1)-(b2*sum_x2))/n

    coefficients = (a,b1,b2)
    return coefficients

def create_plot(x, y, z, coefficients):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='red')
    x_surf = np.linspace(min(x), max(x), 100)
    y_surf = np.linspace(min(y), max(y), 100)
    x_surf, y_surf = np.meshgrid(x_surf, y_surf)
    z_surf = coefficients[0] + coefficients[1]*x_surf + coefficients[2]*y_surf
    ax.plot_surface(x_surf, y_surf, z_surf, color='blue', alpha=0.5)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def on_button_click():
    x = list(map(float, entry_x.get().split(',')))
    y = list(map(float, entry_y.get().split(',')))
    z = list(map(float, entry_z.get().split(',')))
    coefficients = calculate_coefficients(x,y,z)
    fig = create_plot(x, y, z, coefficients)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_result = tk.Label(f3, text=f"Koefisien: {coefficients}")
    label_result.pack()
    label_equation = tk.Label(f3, text=f"Persamaan: z = {coefficients[0]} + {coefficients[1]}x + {coefficients[2]}y")
    label_equation.pack()

label_judul = tk.Label(f1, text="Regresi Linier Berganda", font= ("Comic n Sans", 30, "bold"), fg="maroon")
label_judul.pack()

label_anggota = tk.Label(f1, text="ANGGOTA KELOMPOK : ", font= ("Arial", 10 , "bold"), fg="Black")
label_anggota.pack()

label_nama1 = Label (f1, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama1.pack()
label_nama2 = Label (f1, text="Nama: Tirza Aurellia Wijaya, NIM: 24060122130047", font= ("Arial", 10), fg="Black")
label_nama2.pack()
label_nama3 = Label (f1, text="Nama: Arifatul Mayya Kholidha, NIM: 24060122120003", font= ("Arial", 10), fg="Black")
label_nama3.pack()
label_nama4 = Label (f1, text="Nama: Adinda Rizka Hamdasati, NIM: 24060122140139", font= ("Arial", 10), fg="Black")
label_nama4.pack()
label_nama5 = Label (f1, text="Nama: Alya Safina, NIM: 24060122140123", font= ("Arial", 10), fg="Black")
label_nama5.pack()

label_x = tk.Label(f2, text="Masukkan nilai x (pisahkan dengan koma):")
label_x.pack()
entry_x = tk.Entry(f2)
entry_x.pack()

label_y = tk.Label(f2, text="Masukkan nilai y (pisahkan dengan koma):")
label_y.pack()
entry_y = tk.Entry(f2)
entry_y.pack()

label_z = tk.Label(f2, text="Masukkan nilai z (pisahkan dengan koma):")
label_z.pack()
entry_z = tk.Entry(f2)
entry_z.pack()

button = tk.Button(f2, text="Hitung Koefisien dan Buat Grafik", command=on_button_click)
button.pack()

root.mainloop()
