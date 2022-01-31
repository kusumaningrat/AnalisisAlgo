import os, csv
# import klu
from itertools import permutations

import lobarRoute
from Main import *
import Dashoard
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

def daftar_kota_lobar():
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
        lobarRoute.menu_kota_mataram()
        lobarRoute.tsp(lobarRoute, start)
        lobarRoute.hasil_lintasan_lobar()
    elif pilihan == '0':
        confirm = input("Apakah anda yakin untuk keluar ? [y/n]")
        if confirm == 'y':
            main_menu()
        else:
            Dashoard.dashboard()
    else:
        Dashoard.dashboard()

  
def menu_kota_lobar():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Selaparang".ljust(104)+"||")
    print("||"+"1 = Ampenan".ljust(104)+"||")
    print("||"+"2 = Sekarbela".ljust(104)+"||")
    print("||"+"3 = Sandubaya".ljust(104)+"||")
    print("||"+"4 = Cakranegara".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# mataram
def lobar(lombok_barat_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_barat_route)):
        if point != start:
            tampung_point.append(point)
    min_cost = 1000000
    tampung_permutasi = permutations(tampung_point)
    for permutasi in tampung_permutasi:
        kota_awal(start)
        lintasan+="-->"
        current_cost = 0
        baris = start
        for kolom in permutasi:
            kota_tengah(kolom)
            current_cost += lombok_barat_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_barat_route[baris][start]
        lintasa_copy = lintasan
        if current_cost == min_cost:
            lintasan_tsp.append(lintasa_copy)
        elif current_cost < min_cost:
            lintasan_tsp.clear()
            lintasan_tsp.append(lintasa_copy)
        min_cost = min(min_cost, current_cost)
        lintasan = ""
    return min_cost,lintasan, lintasan_tsp

def kota_awal(start):
    global lintasan
    if start == 0:
        lintasan += "Selaparang"
    elif start == 1:
        lintasan += "Ampenan"
    elif start == 2:
        lintasan += "Sekarbela"
    elif start == 3:
        lintasan += "Sandubaya"
    elif start == 4:
        lintasan += "Cakranegara"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Selaparang-->"
    elif kolom == 1:
        lintasan+="Ampenan-->"
    elif lintasan == 2:
        lintasan+="SEkarbela-->"
    elif kolom == 3:
        lintasan+="Sandubaya-->"
    elif kolom == 4:
        lintasan+="Cakranegara-->"

def hasil_lintasan_lobar():
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = lobar(lombok_barat_route, start)[0]/pertamax
    total_biaya = lobar(lombok_barat_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", lobar(lombok_barat_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(lobar(lombok_barat_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", lobar(lombok_barat_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    Dashoard.dashboard()

def detail():
    kota = ["Selaparang", "Ampenan", "Sekarbela", "Sandubaya", "Sandubaya"]
    menu_kota_lobar()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_barat_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_barat_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)







