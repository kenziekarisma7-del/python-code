print("===MENU MINUMAN===")
print("1.ES TEH")
print("2.ES JERUK")
print("3.KOPI")
print("4.SUSU")
 
pilih = int(input("masukkan minuman yang anda inginkan: "))
 
match pilih:
     case 1:
        print("1.ES TEH")
        print("Harga Rp 5.000")
     case 2:
        print("2.ES JERUK")
        print("Harga Rp 7.000")
     case 3:
        print("3.KOPI")
        print("Harga Rp 8.000")
     case 4:
        print("4.SUSU")
        print("Harga Rp 6.000")
     case _: 
        print("PILIHAN ANDA TIDAK TERSEDIA")