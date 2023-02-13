import os
import time
os.system("clear")
while True :
    print(5*"-"+"PROGRAM KALKULATOR SEDERHANA"+5*"-")
    print(f"""Menu :
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Perpangkatan
6. Sisa Pembagian(Modulus)
7. Total Pembagian(Floor Devision)
""")
    menu = int(input("Silahkan Pilih 1/2/3/4/5/6/7 : "))
    if menu == 1:
        while True:
            print(5*"="+"Anda memilih Penjumlahan"+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Angka : "))
            jumlah= angka1 + angka2
            print("\nHasil:")
            print(f"{angka1} + {angka2} = {jumlah}")
            pilih= input("\nApakah anda ingin mengganti menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()               
    elif menu == 2:
        while True:
            print(5*"="+"Anda Memilih Pengurangan"+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Angka : "))
            jumlah= angka1 - angka2
            print("\nHasil:")
            print(f"{angka1} - {angka2} = {jumlah}")
            pilih= input("\nApakah Anda Ingin Mengganti Menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()
    elif menu == 3:
        while True:
            print(5*"="+"Anda Memilih Perkalian"+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Angka : "))
            jumlah= angka1 * angka2
            print("\nHasil:")
            print(f"{angka1} * {angka2} = {jumlah}")
            pilih= input("\nApakah Anda Ingin Mengganti Menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()
    elif menu == 4:
        while True:
            print(5*"="+"Anda Memilih Pembagian"+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Angka : "))
            jumlah= angka1 / angka2
            print("\nHasil:")
            print(f"{angka1} / {angka2} = {jumlah}")
            pilih= input("\nApakah Anda Ingin Mengganti Menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()
    elif menu == 5:
        while True:
            print(5*"="+"Anda Memilih Perpangkatan "+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Pangkat : "))
            jumlah= angka1 ** angka2
            print("\nHasil:")
            print(f"{angka1} ** {angka2} = {jumlah}")
            pilih= input("\nApakah Anda Ingin Mengganti Menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()
    elif menu == 6:
        while True:
            print(5*"="+"Anda Memilih Modulus"+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Angka : "))
            jumlah= angka1 % angka2
            print("\nHasil:")
            print(f"{angka1} % {angka2} = {jumlah}")
            pilih= input("\nApakah Anda Ingin Mengganti Menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()
    elif menu == 7:
        while True:
            print(5*"="+"Anda Memilih Floor Devision"+5*"="+"\n")
            angka1= float(input("Masukkan Angka : "))
            angka2= float(input("Masukkan Angka : "))
            jumlah= angka1 // angka2
            print("\nHasil:")
            print(f"{angka1} // {angka2} = {jumlah}")
            pilih= input("\nApakah Anda Ingin Mengganti Menu ? (y/n/stop) : ").title()
            if pilih == "Y":
                os.system("clear")
                break
            elif pilih == "N":
                os.system("clear")
                pass
            else:
                print("\n\n\nKarena Anda Tolol, Jadi...\n\n"+5*"="+"PROGRAM DIHENTIKAN"+5*"="+"\n")
                exit()
    else:
        print("\n\nGa Ada Kocak !!\nSilahkan Pilih Kembali !\n")
        time.sleep(1.5)
        os.system("clear")
        continue

#jika pilih no maka akan muncul input apakah anda ingin mengganti menu ?
#jika yes maka .title()akan muncul pilihan menu kembali, jika no maka program akan close