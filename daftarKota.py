import os
import mataramRoute
import Dashoard
import Main

mataram_route = [
    [0,1,2,3,4],
    [1,0,4.3,6.9,7.8],
    [2,4.3,0,4.7,11],
    [3,6.9,4.7,0,12],
    [4,7.8,11,12,0]
]


def daftar_kota_mataram(mataram_route, start):
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
        mataramRoute.menu_kota_mataram()
        mataramRoute.mataram(mataram_route, start)
        mataramRoute.hasil_lintasan_mtr()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            Main.main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()