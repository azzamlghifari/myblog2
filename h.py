def hitung_segiempat():
    width = float(input("Masukkan lebar segiempat: "))
    height = float(input("Masukkan tinggi segiempat: "))
    luas = width * height
    keliling = 2 * (width + height)
    print(f"Luas segiempat: {luas}")
    print(f"Keliling segiempat: {keliling}")

hitung_segiempat()


def hitung_kecepatan():
    jarak = float(input("Masukkan jarak (km): "))
    waktu = float(input("Masukkan waktu (jam): "))
    kecepatan = jarak / waktu
    print(f"Kecepatan rata-rata: {kecepatan} km/jam")

hitung_kecepatan()


def proyeksi_populasi():
    populasi_awal = 250_000_000
    detik_per_tahun = 365 * 24 * 60 * 60
    
    kelahiran_per_tahun = detik_per_tahun // 7
    kematian_per_tahun = detik_per_tahun // 13
    imigrasi_per_tahun = detik_per_tahun // 45
    
    populasi = populasi_awal
    
    for tahun in range(1, 6):
        populasi += kelahiran_per_tahun - kematian_per_tahun + imigrasi_per_tahun
        print(f"Populasi setelah {tahun} tahun = {populasi:,}")

proyeksi_populasi()


width = 5
height = 10
luas = width * height
print(f"Luas segiempat: {luas}")


Luas segiempat: 50


def jumlahkan_digit(n):
    # Basis rekursi: jika n adalah 0, maka jumlah digit adalah 0
    if n == 0:
        return 0
    # Ambil digit terakhir dan tambahkan dengan hasil rekursif dari digit sebelumnya
    return n % 10 + jumlahkan_digit(n // 10)

# Input dari pengguna
angka = int(input("Masukkan bilangan bulat (0-1000): "))
if 0 <= angka <= 1000:
    hasil = jumlahkan_digit(angka)
    print(f"Jumlah digit dari {angka} adalah {hasil}")
else:
    print("Bilangan harus antara 0 hingga 1000!")


def hitung_total_belanja():
    total_belanja = float(input("Masukkan total belanja: Rp"))
    
    if total_belanja < 150_000:
        diskon = 0
    elif 150_000 <= total_belanja <= 249_999:
        diskon = 0.10
    else:
        diskon = 0.20
    
    total_diskon = total_belanja * diskon
    total_bayar = total_belanja - total_diskon
    
    print(f"Diskon: Rp{total_diskon:,}")
    print(f"Total yang harus dibayar: Rp{total_bayar:,}")

hitung_total_belanja()


def cek_kelulusan():
    nilai1 = float(input("Masukkan nilai mata kuliah 1: "))
    nilai2 = float(input("Masukkan nilai mata kuliah 2: "))
    nilai3 = float(input("Masukkan nilai mata kuliah 3: "))
    
    rata_rata = (nilai1 + nilai2 + nilai3) / 3
    
    if rata_rata > 60:
        if nilai1 < 50 or nilai2 < 50 or nilai3 < 50:
            print("Tidak lulus karena ada nilai di bawah 50.")
        else:
            print("Selamat, Anda lulus!")
    else:
        print("Tidak lulus karena rata-rata kurang dari atau sama dengan 60.")

cek_kelulusan()


def kalkulator():
    print("Pilih operasi:")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    if pilihan == 1:
        hasil = angka1 + angka2
        print(f"Hasil pertambahan: {hasil}")
    elif pilihan == 2:
        hasil = angka1 - angka2
        print(f"Hasil pengurangan: {hasil}")
    elif pilihan == 3:
        hasil = angka1 * angka2
        print(f"Hasil perkalian: {hasil}")
    elif pilihan == 4:
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil pembagian: {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Pilihan tidak valid.")

kalkulator()
