import os, csv
import Dashoard
# import klu
from itertools import permutations
lintasan=""
database="database.csv"
data_salesman = []
data_user = []
tampung_username = []
tampung_password = []

lombok_barat_route=[
    [0,1,2,3,4],
    [1,0,22,26,23],
    [2,22,0,5.8,11],
    [3,26,5.8,0,12],
    [4,23,11,12,0]
   
]

lombok_tengah_route=[
    [0,1,2,3,4],
    [1,0,14.2,25.3,17.7],
    [2,14.2,0,18,7.8],
    [3,25.3,18,0,9.6],
    [4,17.7,7.8,9.6,0]  
]

lombok_utara_route=[
    [0,1,2,3,4,5],
    [1,0,45,32,62,47],
    [2,45,0,27,31,17],
    [3,32,27,0,44,30],
    [4,62,31,44,0,14],
    [5,47,17,30,14,0]
]

lombok_timur_route=[
    [0,1,2,3,4],
    [1,0,51,38,21],
    [2,51,0,16,36],
    [3,38,16,0,25],
    [4,21,36,25,0]
   
]

mataram_route = [
    [0,1,2,3,4],
    [1,0,4.3,6.9,7.8],
    [2,4.3,0,4.7,11],
    [3,6.9,4.7,0,12],
    [4,7.8,11,12,0]
]

try:
    with open("database.csv", "r") as cswrite:
        reader = csv.reader(cswrite, delimiter=",")
        for baris in reader:
            data_salesman.append(baris)
except:
    pass
# main tidak perlu dirubah
def main_menu():
    os.system("clear")
    print("="*108)
    print("||"+"Ninjago ".center(104)+"||")
    print("||"+"Selamat Datang di Aplikasi Ninjago".center(104)+"||")
    print("||"+"Silahkan login jika anda telah memiliki akun".center(104)+"||")
    print("||"+"dan Silahkan mendaptar jika belum memiliki akun".center(104)+"||")
    print("="*108)
    print("||"+"[1] Masuk ".ljust(103)+"||")
    print("||"+"[2] Daftar".ljust(103)+"||")
    print("||"+"[3] Keluar".ljust(103)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilih = input("Masukan pilihan anda: ")
    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "3":
        exit()

 
# dashboar tidak perlu dirubah

# daftar kota tidak perlu diruba


def register():
    os.system("clear")
    errors = 0
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    username = input(" Usnername    :")
    password = input(" Password     :")
    if username.isalnum() == False or password.isalnum() == False:
        errors += 1
        print("Username atau password hanya berupa huruf dan angka saja")
    if len(username) < 5 or len(password) < 5:
        errors += 1
        print("Username atau password minimal terdiri dari 6 karakter")
    if username == password:
        errors = 1
        print("Username dan password tidak boleh sama")
    if errors == 0:
        data_salesman.append([username, password])
        with open("database.csv", "a", newline="") as css:
            write = csv.writer(css, delimiter=",")
            for t in data_salesman:
                write.writerow(t)
        print("Akun anda berhasil dibuat, silahkan login1")
    input("Tekan enter untuk kembali")
    main_menu() 

def login():
    os.system("clear")
    print("="*108)
    print("||"+"Ninjago".center(104)+"||")
    print("="*108)
    nama = []
    sandi = []
    with open("database.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            for row in csv_reader:
                nama.append(row[0])
                sandi.append(row[1])
        except:
            pass
    username = input("Username :")
    password = input("Password :")
    if username in nama:
        index = nama.index(username)
        if password == sandi[index]:
            Dashoard.dashboard()
        else:
            print("Password anda salah")
    else:
        print("Akun tidak ditemukan")
    input("Enter untuk kembali")
    main_menu()
    

if __name__ == "__main__":
    main_menu()





