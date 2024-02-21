import tkinter as tk
from tkinter import messagebox
import math

def least_squares_poly2():
    x_values = list(map(float, entry_x.get().split(',')))
    y_values = list(map(float, entry_y.get().split(',')))
    n = len(x_values)
    x = x_values
    y = y_values
    A = [[n, sum(x), sum(i**2 for i in x)], [sum(x), sum(i**2 for i in x), sum(i**3 for i in x)], [sum(i**2 for i in x), sum(i**3 for i in x), sum(i**4 for i in x)]]
    b = [sum(y), sum(i*j for i, j in zip(x, y)), sum(i*j for i, j in zip([i**2 for i in x], y))]
    a, b, c = gauss_seidel(A, b)
    result.set(f"Persamaan polinomialnya adalah: y = {a} + {b}x + {c}x²")

def gauss_seidel(A, b, eps=1e-10, max_iter=1000):
    x = [0, 0, 0]
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(len(A)):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            x_new[i] = (b[i] - s1) / A[i][i]
        if all(abs(x_new[i]-x[i]) < eps for i in range(len(x))):
            return x_new
        x = x_new
    return x

root = tk.Tk()
root.title("Least Squares Polynomial Degree 2")

frame = tk.Frame(root)
frame.pack()

label_judul = tk.Label(frame, text="LEAST SQUARES POLYNOMIAL DEGREE 2", font= ("Comic n Sans", 30, "bold"), fg="maroon")
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


label_x = tk.Label(frame, text="\nMasukkan nilai-nilai x (pisahkan dengan koma):")
label_x.pack()
entry_x = tk.Entry(frame , width=100)
entry_x.pack()

label_y = tk.Label(frame, text="Masukkan nilai-nilai y (pisahkan dengan koma):")
label_y.pack()
entry_y = tk.Entry(frame, width=100 )
entry_y.pack()

result = tk.StringVar()
label_result = tk.Label(frame, textvariable=result)
label_result.pack()

button = tk.Button(frame, text="Hitung", command=least_squares_poly2)
button.pack()

root.mainloop()