print("===TENTUKAN KATEGORI UJIAN===")
print("1.TEORI")
print("2.PRAKTIK")

kategori = int(input("masukkan kategori yang anda pilih: "))

match kategori:
     case 1:
         print("TEORI")
     case 2:
         print("PRAKTIK")
     case _:
         print("kategori tidak valid")

nilai = int(input("masukkan nilai anda: "))

if nilai >= 75:
    print("SELAMAT ANDA LULUS")
else: 
    print("MAAF ANDA BELUM LULUS")