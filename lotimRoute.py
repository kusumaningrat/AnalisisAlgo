import os, csv
import Dashoard
import Kota
# import klu
from itertools import permutations
# lombok timur
def lotim(lombok_timur_route, start):
    global lintasan
    tampung_point = []
    lintasan_tsp = []
    for point in range(len(lombok_timur_route)):
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
            current_cost += lombok_timur_route[baris][kolom]
            baris = kolom
        kota_awal(start)
        current_cost +=lombok_timur_route[baris][start]
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
        lintasan += "Aikmel"
    elif start == 1:
        lintasan += "Jerowaru"
    elif start == 2:
        lintasan += "Keruak"
    elif start == 3:
        lintasan += "Labuhan haji"
    elif start == 4:
        lintasan += "Masbagik"

def kota_tengah(kolom):
    global lintasan
    if kolom == 0:
        lintasan+="Aikmel-->"
    elif kolom == 1:
        lintasan+="Jerowaru-->"
    elif lintasan == 2:
        lintasan+="Keruak-->"
    elif kolom == 3:
        lintasan+="Labuhan haji-->"
    elif kolom == 4:
        lintasan+="Masbagik-->"

def hasil_lintasan_lotim(lombok_timur_route, start):
    cost_bbm = 1000
    pertamax = 4
    jmlh_pertamax = lotim(lombok_timur_route, start)[0]/pertamax
    total_biaya = lotim(lombok_timur_route, start)[0]/pertamax*cost_bbm
    print("="*108)
    print("||"+"Kesimpulan".center(104)+"||")
    print("="*108)
    print("||"+" Lintasan Terpendek : ", lotim(lombok_timur_route, start)[0], "km".ljust(74)+"||")
    print("||"+" Menghabiskan Pertamax : ", jmlh_pertamax, "liter".ljust(72)+"||")
    print("||"+" Total Biaya : ", total_biaya, "liter".ljust(68)+"||")
    for i in range(len(lotim(lombok_timur_route, start)[2])):
        print("||"+" Lintasan yang dilalui : ", lotim(lombok_timur_route,start)[2][i].ljust(77)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    input("Tekan enter untuk kembali")
    Dashoard.dashboard()

def detail_route_lotim(lombok_timur_route, start):
    kota = ["Aikmel", "Jerowaru", "Keruak", "Labuhan haji", "Masbagik"]
    Kota.menu_lombokTimur()
    input("Tekan untuk melihat route")
    print("="*108)
    print("||"+"Detail route".center(104)+"||")
    print("="*108)
    for i in range(len(lombok_timur_route)):
        cost = str(kota[start])+"-->"+str(kota[i])+" = "+str(lombok_timur_route[start][i])+" km"
        print("||"f' {cost}'.ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
