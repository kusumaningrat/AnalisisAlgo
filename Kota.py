import os, csv

def menu_lombokTengah():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Janapria".ljust(104)+"||")
    print("||"+"1 = Kopang".ljust(104)+"||")
    print("||"+"2 = Pringgarata".ljust(104)+"||")
    print("||"+"3 = Batukliang".ljust(104)+"||")
    print("||"+"4 = Praya".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
    
# lintasan lombok utara
def menu_lombokUtara():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"1 = Bayan".ljust(104)+"||")
    print("||"+"2 = Gangga".ljust(104)+"||")
    print("||"+"3 = Kayangan".ljust(104)+"||")
    print("||"+"4 = Pemenang".ljust(104)+"||")
    print("||"+"5 = Tanjung".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
  
# Lintasan lmbok Barat
def menu_lombokBarat():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Narmada".ljust(104)+"||")
    print("||"+"1 = Kediri".ljust(104)+"||")
    print("||"+"2 = Labuapi".ljust(104)+"||")
    print("||"+"3 = Gerung".ljust(104)+"||")
    print("||"+"4 = Lembar".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))
  
# lintasan lombok timur
def menu_lombokTimur():
    os.system("clear")
    global start
    print("||"+"Daftar Menu Kota".center(104)+"||")
    print("="*108)
    print("||"+"0 = Aikmel".ljust(104)+"||")
    print("||"+"1 = Jerowaru".ljust(104)+"||")
    print("||"+"2 = Keruak".ljust(104)+"||")
    print("||"+"3 = Labuhan haji".ljust(104)+"||")
    print("||"+"4 = Masbagik".ljust(104)+"||")
    print("="*108)
    print("||"+"Travelling Salesman Problem".center(104)+"||")
    print("="*108)
    start = int(input("Masukan titik awal: "))

# lintasan kota mataram 
def menu_kota_mataram():
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