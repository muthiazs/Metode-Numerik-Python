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
