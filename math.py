import math
def menu():
    print("|====================================|")
    print("|            1.Penjumlahan           |")
    print("|            2.Pengurangan           |")
    print("|            3.Perkalian             |")
    print("|            4.Pembagian             |")
    print("|            5.Barisan Aritmatika    |")
    print("|            6.Deret Aritmatika      |")
    print("|            7.Barisan Geometri      |")
    print("|            8.Deret Geometri        |")
    print("|            9.Pythagoras a          |")
    print("|            10.Pythagoras b         |")
    print("|            11.Pythagoras c         |")
    print("|            12.Triple Pythagoras    |")
    print("|====================================|")

menu()
pilih = input("Masukan Menu Program Diatas : ")

def tambah():
    print("Penjumlahan")
    a = int(input("Masukan Angka Pertama : "))
    b = int(input("Masukan Angka Kedua : "))
    hasil1 = a + b
    print("Hasilnya Adalah : ",hasil1)
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def kurang():
    print("Pengurangan")
    a = int(input("Masukan Angka Pertama : "))
    b = int(input("Masukan Angka Kedua : "))
    hasil2 = a - b
    print("Hasilnya Adalah : ",hasil2)
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def kali():
    print("Perkalian")
    a = int(input("Masukan Angka Pertama : "))
    b = int(input("Masukan Angka Kedua : "))
    hasil3 = a * b
    print("Hasilnya Adalah : ",hasil3)
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def bagi():
    print("Pembagian")
    a = int(input("Masukan Angka Pertama : "))
    b = int(input("Masukan Angka Kedua : "))
    if b != 0:
        hasil4 = a / b
    else:
        print("Tidak Terdefinisi. Tidak boleh pembagian dengan nol")
    print("Hasilnya Adalah : ",hasil4)
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def aritmatika1():
    print("Barisan Aritmatika")
    print("Un = a + (n-1)b")
    a = int(input("Masukan suku pertama : "))
    b = int(input("Masukan beda(U2 - U1) : "))
    n = int(input("Masukan suku ke-n : "))
    Un = a + (n-1) * b
    print(f"Suku Ke {n} Adalah : {Un}")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def aritmatika2():
    print("Deret Aritmatika")
    print("Sn = n/2 (2a + (n-2)b)")
    a = int(input("Masukan suku pertama : "))
    b = int(input("Masukan beda(U2 - U1) : "))
    n = int(input("Masukan suku ke-n : "))
    Sn = n/2 * (2*a + (n-1) * b)
    print(f"Jumlah {n} Suku Pertama Adalah : {Sn}")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")


def geometri1():
    print("Barisan Geometri")
    print("Un = a.r^n-1")
    a = int(input("Masukan suku pertama : "))
    r = int(input("Masukan rasio(U2 / U1) : "))
    n = int(input("Masukan suku ke-n : "))
    Un = a*r**(n-1)
    print(f"Suku Ke {n} Adalah : {Un}")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def geometri2():
    print("Deret Geometri")
    print("Sn = a(r^n-1) / r - 1 | Sn = a(1-r^n) / 1 - r")
    a = int(input("Masukan suku pertama : "))
    r = int(input("Masukan rasio(U2 / U1) : "))
    n = int(input("Masukan suku ke-n : "))
    if r > 1:
        batas_atas = a * (r**n)
        batas_bawah = r - 1
        Sn1 = batas_atas / batas_bawah
        print(f"Jumlah {n} Suku Pertama Adalah : {Sn1}")
    elif r < 1:
        batas_atas2 = a * (1 - r**n)
        batas_bawah2 = 1 - r
        Sn = batas_atas2 / batas_bawah2
        print(f"Jumlah {n} Suku Pertama Adalah : {Sn}")
    else:
        print("Error rasio tidak boleh nol!")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def pythagorasA():
    print("Pythagoras Mencari Nilai a")
    print("a^2 = Vb^2-c^2")
    c = int(input("Masukan c : "))
    b = int(input("Masukan b : "))
    a = math.sqrt(c**2 - b**2)
    print(f"Sisi a Adalah : {a}")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def pythagorasB():
    print("Pythagoras Mencari Nilai b")
    print("b^2 = Vc^2-a^2")
    c = int(input("Masukan c : "))
    a = int(input("Masukan a : "))
    b = math.sqrt(c**2 - a**2)
    print(f"Sisi b Adalah : {b}")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def pythagorasC():
    print("Pythagoras Mencari Nilai c")
    print("c^2 = Va^2+b^2")
    a = int(input("Masukan a : "))
    b = int(input("Masukan b : "))
    c = math.sqrt(a**2 + b**2)
    print(f"Sisi c Adalah : {c}")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

def triplePy():
    print("Triple Pythagoras")
    a = int(input("Masukan a : "))
    b = int(input("Masukan b : "))
    c = int(input("Masukan c : "))
    if a**2 + b**2 == c**2:
        print("Segitiga Siku-Siku")
    elif c**2 < a**2 + b**2:
        print("Segitiga Tumpul")
    elif c**2 > a**2 + b**2:
        print("Segitiga Lancip")
    else:
        print("MASUKAN ANGKA DENGAN BENAR!")
    back = str(input("Ketik y jika ingin melihat program lain : "))
    if back == ('y'):
        menu()
        pilih = input("Masukan Menu Program Diatas : ")
        if pilih == '1':
            tambah()

        elif pilih == '2':
            kurang()

        elif pilih == '3':
            kali()

        elif pilih == '4':
            bagi()

        elif pilih == '5':
            aritmatika1()

        elif pilih == '6':
            aritmatika2()

        elif pilih == '7':
            geometri1()

        elif pilih == '8':
            geometri2()

        elif pilih == '9':
            pythagorasA()

        elif pilih == '10':
            pythagorasB()

        elif pilih == '11':
            pythagorasC()

        elif pilih == '12':
            triplePy()

        else:
            print("Program Tidak Ada")

if pilih == '1':
    tambah()

elif pilih == '2':
    kurang()

elif pilih == '3':
    kali()

elif pilih == '4':
    bagi()

elif pilih == '5':
    aritmatika1()

elif pilih == '6':
    aritmatika2()

elif pilih == '7':
    geometri1()

elif pilih == '8':
    geometri2()

elif pilih == '9':
    pythagorasA()

elif pilih == '10':
    pythagorasB()

elif pilih == '11':
    pythagorasC()

elif pilih == '12':
    triplePy()

else:
    print("Program Tidak Ada")