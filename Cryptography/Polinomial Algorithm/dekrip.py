import numpy as np

# Data y dari soal
y_values = np.array([
    27992, 28739, 21574, 31593, 29535, 29800, 26995, 24432, 28524, 
    31086, 28525, 26977, 27743, 25705, 26214, 26979, 30060, 29759, 16253
])

# ✅ SOLUSI: Gunakan urutan angka sederhana untuk x, BUKAN angka aslinya.
x_values = np.arange(len(y_values))

# Derajat polinomial adalah jumlah titik - 1
degree = len(x_values) - 1

# Hitung koefisien dengan input yang stabil
coefficients = np.polyfit(x_values, y_values, degree)

# Ubah koefisien menjadi flag
flag = ""
for coeff in reversed(coefficients):
    flag += chr(int(round(coeff)))

# Tampilkan hasil akhir
print(f"✅ Flag yang ditemukan: {flag}")