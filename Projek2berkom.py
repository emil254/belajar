import random
Kode_pesanan = random.randint (10000, 100000)
i= 0
j = 0
k = 0
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
kategori_makanan = ["Jus atau buah-buahan", "Ice cream, susu, dan youghurt", "Makanan berat", "Snack ringan"]
locker_hangat = ["01","02","03","04","05"]
locker_dingin = ["06","07","08","09","10"]
kesempatank = 3
kesempatanc = 3
kode_output = str(Kode_pesanan)
print("Dalam aplikasi")
print("Sisi Kurir")
print("Ini adalah kode locker: ", kode_output)
print("Sisi Customer")
print("Ini adalah kode locker: ", kode_output)
kode_customer = str(input(f"Buatlah kodemu dengan terdapat dengan format (XX{kode_output}YY): "))

print("Pada Locker")
identitas = str(input("Apakah anda customer atau kurir: "))
while True:
    if identitas == "kurir":
        print("Sisi Kurir")
        hari_ini = str(input("Hari ini: "))
        if hari_ini == hari[6]:
            hari_lanjut = "Senin"
        else:
            for k in range (0,6):
                if hari_ini != hari[k]:
                    k = k+1
                else:
                    hari_lanjut = hari[k+1]
                    break
        jam_antar = int(input("Pukul berapa anda memasukkan pesanan: "))
        menit_antar = int(input("Menit berapa anda memasukkan pesanan: "))
        print("Berikut adalah kategori makanan")
        print(f"1. {kategori_makanan[0]} (ketik 1)")
        print(f"2. {kategori_makanan[1]} (ketik 2)")
        print(f"3. {kategori_makanan[2]} (ketik 3)")
        print(f"4. {kategori_makanan[3]} (ketik 4)")
        pilih_kategori = str(input("Pilih kategori makanan: "))
        while kesempatank > 0:
            kode = str(input("Silahkan masukkan kode pesanan: "))
            if kode == kode_output:
                if pilih_kategori == "1":
                    print(f"Masukkan makanan pada locker ke-{locker_dingin[i]}")
                    i = i + 1
                elif pilih_kategori == "2":
                    print(f"Masukkan makanan pada locker-{locker_dingin[i]}")
                    i = i + 1
                elif pilih_kategori == "3":
                    print(f"Masukkan makanan pada locker-{locker_hangat[j]}")
                    j = j + 1
                else:
                    print(f"Masukkan makanan pada locker-{locker_dingin[i]}")
                    i = i +1 
                kurir = True
                break
            else:
                print("Anda salah menginput, silahkan masukkan ulang")
                kesempatank = kesempatank -1
        else:
            print("Kesempatan anda habis, silahkan hubungi cutomer Anda")
            kurir = False
        if kurir == True:
            print("Sisi Customer")
            print("Notifikasi Aplikasi Locker")
            print(f"Pesanan sudah tiba pada {hari_ini}, {jam_antar}.{menit_antar}, silahkan ambil pesananmu sebelum {hari_lanjut}, {jam_antar}.{menit_antar}")
            print("Pada Locker")
            hari_jemput = str(input("Hari ini: "))
            jam_jemput = int(input("Jam berapa kamu mengambil Pesanan: "))
            menit_jemput = int(input("Menit berapa kamu mengambil Pesanan: "))
            if hari_jemput == hari_ini:
                while kesempatanc > 0:
                    kode = str(input("Silahkan masukkan kode pesanan: "))
                    if kode == kode_customer:
                        print("Selamat makan")
                        break
                    else:
                        print("Anda salah menginput, silahkan masukkan ulang")
                        kesempatanc = kesempatanc -1
                else:
                    print("Kesempatan anda habis, silahkan hubungi customer service")
            else: 
                if hari_jemput == hari_lanjut:
                    if (jam_jemput < jam_antar) or (jam_jemput == jam_antar and menit_jemput < menit_antar):
                        while kesempatanc > 0:
                            kode = str(input("Silahkan masukkan kode pesanan: "))
                            if kode == kode_customer:
                                print("Selamat makan")
                                break
                            else:
                                print("Anda salah menginput, silahkan masukkan ulang")
                                kesempatanc = kesempatanc -1
                        else:
                            print("Kesempatan anda habis, silahkan hubungi customer service")
                    else:
                        print("Yah, makanannya sudah diangkut petugas") 
        else:
            print("NOTIFIKASI APLIKASI LOKER")
            print("Hati-hati, sepertinya ada kurir yang menyamar, silahkan hubungi kurir")
        break
    else:
        print("Sebentar ya, kurir belum tiba")
        identitas = str(input("Apakah anda customer atau kurir: "))





