total_nilai = 0
jumlah_data=5
for i in range(5):
    angka = int(input(f"Masukkan nilai ke-{i+1}: "))
    total_nilai += angka
rata_nilai=total_nilai/jumlah_data
print("Nilai rata-rata:",rata_nilai) 
