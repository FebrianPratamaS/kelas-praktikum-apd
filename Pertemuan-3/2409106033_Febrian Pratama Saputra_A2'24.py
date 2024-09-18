# Percabangan
Umur = int(input("Masukkan umur Anda : "))
if Umur > 0:
    if Umur <= 10:
        print("Umur Anda termasuk kategori anak-anak")
    elif Umur <= 18:
        print("Umur Anda termasuk kategori remaja")
    elif Umur <=35:
        print("Umur Anda termasuk kategori dewasa")
    elif Umur <=65:
        print("Umur Anda termasuk kategori paruh baya")
    else:
        print("Umur Anda termasuk kategori Tua")
else:
    print("Umur harus bilangan positif")

# Ternary 1
angka = int(input("Masukkan angka: "))
result = "Genap" if angka % 2 == 0 else "Ganjil"
print(angka, "adalah angka",result)

#Studi Kasus 1
harga = float(input("Masukkan harga barang = "))
jumlah = float(input("Masukkan jumlah barang = " ))
diskon = 0.20
harga_total = harga * jumlah

if harga_total > 100000 and jumlah >= 5:
    diskon_barang = harga_total * diskon
    harga_diskon = harga_total - diskon_barang
    print(f"Harga setelah diskon adalah Rp{harga_diskon:.0f}")

else:
    print("Anda tidak mendapatkan diskon.")

# Ternary 2 / Studi Kasus 2
# Pak Kades sedang mendata penduduknya berdasarkan jenis kelamin, buatlah program
# sederhana untuk menentukan jenis kelamin seseorang dengan menggunakan ternary
# operator.

nama = input("Masukkan nama: ")
kelamin = input("Masukkan jenis kelamin (L untuk Laki-laki, P untuk Perempuan): ")
jenis_kelamin = "Laki-laki" if kelamin == "L" else "Perempuan" if kelamin == "P" else "Tidak diketahui"
print(f"{nama} adalah {jenis_kelamin}.")

#MatchCase
print("""
    ========================
    Kalkulator Sederhana
    1. +
    2. -
    3. *
    4. /  
    =======================""")
fitur = int(input("Pilih Fitur : "))

match fitur:
    case 1:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a + b
        print(f"Hasil Pertambahan Angka 1 dan Angka 2 adalah {c}")
    case 2:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a - b
        print(f"Hasil Pengurangan Angka 1 dan Angka 2 adalah {c}")
    case 3:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a * b
        print(f"Hasil Perkalian Angka 1 dan Angka 2 adalah {c}")
    case 4:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a / b
        print(f"Hasil Pembagian Angka 1 dan Angka 2 adalah {c}")
    case _:
        print("Invalid Input!")

#Nested Ifs
#Buat program python menggunakan kondisi nested If
#Ketentuan : Terdapat input Nilai
#
# Nilai A == >= 80 (A- : 80 - 89, A+ : 90 - 100)
# Nilai B == >= 70 (B- : 70 - 74, B+ : 75 - 79)
#Buat Else jika Kondisi tidak memenuhi

nilai = int(input("Masukkan Nilai anda: "))

if nilai >= 0 and nilai <= 100:
    if nilai >= 80:
        if nilai >= 90:
            print("Nilai anda adalah A+")
        else:
            print("Nilai anda adalah A-")

    elif nilai >= 70:
        if nilai >= 75:
            print("Nilai anda adalah B+")
        else:
            print ("Nilai anda adalah B-")

    else:
        print("Maaf. Nilai anda terlalu rendah untuk memenuhi syarat.")
elif nilai > 100: 
    print("Kok nilaimu tinggi banar???")
else:
    print("Kok nilaimu negatif???")






