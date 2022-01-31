import os, csv
from tracemalloc import start
import Dashoard
import Main
import Kota
import mataramRoute
import lotimRoute

def daftar_kota():
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
        Kota.menu_kota_mataram()
        mataramRoute.mataram(mataramRoute, start)
        mataramRoute.hasil_lintasan_mtr()
    elif pilihan == '2':
        Kota.menu_lombokTimur()
        lotimRoute.lotim()
        lotimRoute.hasil_lintasan_lotim()
    # elif pilihan == '3':
    #     menu_lombokBarat()
    #     lobar()
    #     hasil_lintasan_lobar()
    # elif pilihan == '4':
    #     menu_lombokTengah()
    #     loteng()
    #     hasil_lintasan_loteng()
    # elif pilihan == '5':
    #     menu_lombokUtara()
    #     klu()
    #     hasil_lintasan_klu()      
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            Main.main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()