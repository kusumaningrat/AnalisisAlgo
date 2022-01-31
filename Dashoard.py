from Main import *
import os
import mataramRoute, lobarRoute

def dashboard():
    os.system("clear")
    print("="*108)
    print("||"+"NinjaGo".center(104)+"||")
    print("="*108)
    print("||"+"    [1] = Mataram".ljust(104)+"||")
    print("||"+"    [2] = lombok Timur".ljust(104)+"||")
    print("||"+"    [3] = lombok Barat".ljust(104)+"||")
    print("||"+"    [4] = lombok Tengah".ljust(104)+"||")
    print("||"+"    [5] = lombok Utara".ljust(104)+"||")
    print("||"+"    [0] = Keluar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    pilihan = input("Masukan pilihan anda : ")
    if pilihan == '1':
        mataramRoute.daftar_kota_mataram()
    elif pilihan == '2':
        lobarRoute.daftar_kota_lobar()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            dashboard()
    else:
        dashboard()