import os
import datetime
import sys
import random
def login():
    correct_username = "admin"
    correct_password = "admin123"
    
    print("---------------------------------------------------------------")
    print("|                          LOGIN                              |")
    print("|Silahkan Login User Terlebih Dahulu Untuk Langkah Selanjutnya|")
    print("---------------------------------------------------------------")
    username = input("Masukkan Nama Pengguna: ")
    password = input("Masukkan Kata Sandi   : ")
    if username == correct_username and password == correct_password:
        os.system('cls')
        menu()
    else:
        os.system('cls')
        print("\033[0;31mNama Pengguna atau Kata Sandi Salah\033[0;0m")
        login()

def menu():
    print("---------------------------------------------------------------")
    print("|                       SELAMAT DATANG                        |")
    print("|    DI APLIKASI PENDAFTARAN RUMAH SAKIT SISTEM INFORMASI     |")
    print("|      Silahkan Input NIK dan Nama Pasien Dengan Teliti       |")
    print("---------------------------------------------------------------")
    nik =(input("Masukkan NIK   : "))
    print("\033[0;31mINPUT NAMA PASIEN DENGAN HURUF KAPITAL\033[0;0m")
    nama =(input("Masukkan Nama  : "))
    
    sukses=False
    file=open("DataPasien.txt", "r")
    for i in file:
        a,b =i.split(",")
        b=b.strip()
        if(a==nik and b==nama):
            sukses=True
            break
    file.close()
    if(sukses):
        os.system('cls')
        pelayanan(nama)
    else:
        os.system('cls')
        print("\033[0;31mPasien Tidak Terdaftar, Silahkan Daftarkan Pasien\033[0;0m")
        daftar()
  
def daftar():
    print("---------------------------------------------------------------")
    print("|                      PENDAFTARAN PASIEN                     |")
    print("|        Masukkan DSata Pasien Dengan Lengkap dan Benar        |")
    print("---------------------------------------------------------------")
    nik =(input("NIK            : "))
    print("\033[0;31mINPUT NAMA PASIEN DENGAN HURUF KAPITAL\033[0;0m")
    nama =(input("Nama           : "))
    kelamin = input("Jenis Kelamin  : ")
    tanggal_lahir = input("Tanggal Lahir  : ")
    alamat = input("Alamat         : ")
    
    file=open("DataPasien.txt", "a")
    file.write("\n"+nik+","+nama)
    os.system("cls")
    pelayanan(nama)
    
def pelayanan(nama):
    print("---------------------------------------------------------------")
    print("|                       JENIS PELAYANAN                       |")
    print("|         Masukkan Jenis Pelayan Yang Pasien Butuhkan         |")
    print("---------------------------------------------------------------")
    print("Daftar Pelayanan:")
    print("  A. Pelayanan Umum")
    print("  B. Pelayanan Anak")
    print("  C. Pelayanan Penyakit Dalam")
    print("  D. Pelayanan Urologi\n")
    pilihan = input("Masukkan Jenis Pelayanan Pasien: ")
    pilihan = pilihan.upper()

    if pilihan == "A":
        jenis="Pelayanan Umum"
        ruang="Ruang 301"
        dokter="Dr. Willy Andryan"
        antrian="A -"
        os.system('cls')
    elif pilihan == "B":
        jenis="Pelayanan Anak"
        ruang="Ruang 303"
        dokter="Dr. Siska Kartikasari"
        antrian="B -"
        os.system('cls')
    elif pilihan == "C":
        jenis="Pelayanan Penyakit Dalam"
        ruang="Ruang 305"
        dokter="Dr. Fitra Hakiki Firdaus"
        antrian="C -"
        os.system('cls')
    elif pilihan == "D":
        jenis="Pelayanan Urologi"
        ruang="Ruang 307"
        dokter="Dr. Bimo Syahlendra"
        antrian="D -"
        os.system('cls')
    else:
        os.system('cls')
        print("\033[0;31mAnda Salah Menginput, Silahkan Ulangi Kembali\033[0;0m")
        pelayanan(nama)

    date=datetime.datetime.now()
   
    print("--------------------------------------")
    print("|    Rumah Sakit Sistem Informasi    |")
    print("|            Kota Bekasi             |")
    print("--------------------------------------")
    print("Nama: %s              \n"%(nama))
    print("              %s              "%(ruang))
    print("         %s                \n"%(dokter))
    print("          Nomor Antrian Anda          ")
    print("              ",antrian,random.randint(0,300),"\n")
    print(date.strftime("         %a %x %X"))
    print("--------------------------------------")

    penutup=input("Apakah Anda Ingin Kembali ke Menu? (Y/N): ")
    penutup=penutup.upper()
    if penutup=="Y":
        os.system('cls')
        menu()
    else:
        os.system('cls')
        sys.exit()
login()