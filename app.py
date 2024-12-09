from msvcrt import getwch
from os import system

def ClearScreen():
    system("cls")

# ClearScreen, getwch


# ------------ Variabel ------------

character_input = ''
nama_menu = ["Nasi", "Ayam Goreng", "Kentang Goreng", "Burger", "Soda", "Air Mineral"]
harga_menu = [9000, 20000, 12000, 21000, 12000, 10000]
banyak_pesanan = [0, 0, 0, 0, 0, 0]

voucher_valid = [1234, 5678, 8567, 4321]
nama_voucher = [                                 \
    "Diskon 15% untuk pembelian ayam goreng",    \
    "Diskon 15% untuk pembelian burger",         \
    "Diskon 10% untuk pembelian kentang goreng", \
    "Diskon 5% untuk pembelian soda"             \
]
diskon_voucher = [0.15, 0.15, 0.10, 0.5]
target_voucher = [1, 3, 2, 4]
voucher_aktif = [False, False, False, False]
ada_voucher_aktif = False

# ------------ Definisi Fungsi ------------

# Fungsi ini menampilkan menu
def PrintMenu():
    for i in range(len(nama_menu)):
        print(f"{i+1}. {nama_menu[i]} | harga: Rp. {harga_menu[i]} | pesanan: {banyak_pesanan[i]}")
    print()
    if ada_voucher_aktif == True:
        print("Voucher aktif:")
        for i in range(len(nama_voucher)):
            if voucher_aktif[i] == True:
                print(nama_voucher[i])
        print()

def LayarTambahPesanan():
    while True:
        # Hapus layar
        ClearScreen()

        # Gambar layar
        PrintMenu()

        print("Masukkan nomor menu yang ingin ditambah, masukkan 0 untuk menyelesaikan")

        # Proses input
        character_input = getwch()

        if not character_input.isdigit():
            continue

        if character_input == '0':
            break

        indeks = int(character_input) - 1

        if indeks < 0 or indeks >= len(nama_menu):
            continue

        banyak_pesanan[indeks] = banyak_pesanan[indeks] + 1

def LayarKurangPesanan():
    while True:
        # Hapus layar
        ClearScreen()

        # Gambar layar
        PrintMenu()

        print("Masukkan nomor menu yang ingin ditambah, masukkan 0 untuk menyelesaikan")

        # Proses input
        character_input = getwch()

        if not character_input.isdigit():
            continue

        if character_input == '0':
            break

        indeks = int(character_input) - 1

        if indeks < 0 or indeks >= len(nama_menu):
            continue

        if banyak_pesanan[indeks] > 0:
            banyak_pesanan[indeks] = banyak_pesanan[indeks] - 1

def LayarKodeVoucher():
    input_angka_voucher = [-1, -1, -1, -1]
    index_angka_voucher = 0
    while True:
        # Hapus layar
        ClearScreen()

        print("Masukkan kode voucher (4 digit angka). Masukkan q untuk kembali")
        print(f'{input_angka_voucher[0] if input_angka_voucher[0] >= 0 else '_'} ', end='')
        print(f'{input_angka_voucher[1] if input_angka_voucher[1] >= 0 else '_'} ', end='')
        print(f'{input_angka_voucher[2] if input_angka_voucher[2] >= 0 else '_'} ', end='')
        print(f'{input_angka_voucher[3] if input_angka_voucher[3] >= 0 else '_'} ')

        if index_angka_voucher > len(input_angka_voucher) - 1:
            break

        character_input = getwch()

        if character_input == 'q':
            return

        if not character_input.isdigit():
            continue

        angka = int(character_input)

        input_angka_voucher[index_angka_voucher] = angka

        index_angka_voucher += 1

    angka_voucher = input_angka_voucher[0] * 1000 + input_angka_voucher[1] * 100 + input_angka_voucher[2] * 10 + input_angka_voucher[3]
    
    global ada_voucher_aktif 
    for i in range(len(voucher_valid)):
        if angka_voucher == voucher_valid[i]:
            print(nama_voucher[i])
            ada_voucher_aktif = True
            if voucher_aktif[i] == True:
                print("Voucher sudah aktif, tekan q untuk kembali")
            else:
                voucher_aktif[i] = True
                print("Voucher benar, tekan q untuk kembali")
            break
    else:
        print("Voucher salah, tekan q untuk kembali")

    c = ''
    while c != 'q':
        c = getwch()
    

# ------------ Algoritma ------------

while True:
    # Hapus layar
    ClearScreen()

    # Gambar layar
    PrintMenu()

    print("Masukkan opsi:")
    print("0. Selesaikan pesanan")
    print("1. Tambah pesanan")
    print("2. Kurang pesanan")
    print("3. Kode voucher")

    # Proses input
    character_input = getwch()

    if character_input == '0':      # input 0, selesaikan pesanan
        break
    elif character_input == '1':    # input 1, ganti menjadi layar tambah pesanan
        LayarTambahPesanan()
    elif character_input == '2':    # input 2, ganti menjadi layar kurang pesanan
        LayarKurangPesanan()
    elif character_input == '3':
        LayarKodeVoucher()

# menghitung harga total, bersihkan layar terlebih dahulu
ClearScreen()
total = [0 for i in range(6)]
for i in range(len(nama_menu)):
    total[i] = banyak_pesanan[i] * harga_menu[i]


if ada_voucher_aktif == True:
    print("Diskon:")
    for i in range(len(voucher_aktif)):
        if voucher_aktif[i] == True:
            total[target_voucher[i]] = total[target_voucher[i]] * (1 - diskon_voucher[i])
            print(nama_voucher[i])
    print()

total_semua = 0
for i in range(len(total)):
    total_semua += total[i]

# Print bill
for i in range(len(nama_menu)):
    if total[i] == 0:
        continue
    print(f"{nama_menu[i]} {banyak_pesanan[i]}X : Rp.{total[i]}")

# print hasil, jika total pesanan Rp 0 dianggap batal memesan
if total_semua > 0:
    print(f"Total harga_menu makanan: Rp. {total_semua}")
else:
    print("Pesanan batal")