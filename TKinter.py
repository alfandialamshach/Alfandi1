import tkinter as tk
import sqlite3

# Import modul PIL untuk memuat gambar
from PIL import ImageTk

# Buat jendela Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")  # Mengatur ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat 10 label dan entry baru untuk 10 mata pelajaran tambahan
label_biologi = tk.Label(root, text="Nilai Biologi: ")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika: ")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris: ")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

label_matematika = tk.Label(root, text="Nilai Matematika: ")
label_matematika.pack()
entry_matematika = tk.Entry(root)
entry_matematika.pack()

label_Electro = tk.Label(root, text="Nilai Electro: ")
label_Electro.pack()
entry_Electro = tk.Entry(root)
entry_Electro.pack()

label_sejarah = tk.Label(root, text="Nilai Sejarah: ")
label_sejarah.pack()
entry_sejarah = tk.Entry(root)
entry_sejarah.pack()

label_mesin = tk.Label(root, text="Nilai Mesin: ")
label_mesin.pack()
entry_mesin = tk.Entry(root)
entry_mesin.pack()

label_seni = tk.Label(root, text="Nilai Seni: ")
label_seni.pack()
entry_seni = tk.Entry(root)
entry_seni.pack()

label_olahraga = tk.Label(root, text="Nilai Olahraga: ")
label_olahraga.pack()
entry_olahraga = tk.Entry(root)
entry_olahraga.pack()

label_Sipil = tk.Label(root, text="Nilai Sipil: ")
label_Sipil.pack()
entry_Sipil = tk.Entry(root)
entry_Sipil.pack()

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi)
button_submit.pack(pady=10)

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil.pack()

# Menambahkan gambar
image = Image.open("logo_universitas.png")
photo_image = ImageTk.PhotoImage(image)
label_logo = tk.Label(root, image=photo_image)
label_logo.pack(pady=10)

root.mainloop()
