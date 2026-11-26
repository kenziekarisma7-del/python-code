print("==jenis pelanggan==")
print("1.member")
print("2.nonmember")

member = int(input("apa anda member: "))

match member:
 case 1:
   print("diskon 10%, jika total belanja >= 100000")
   
 case 2:
   print("diskon 5%, jika total belanja >= 100000")
 case _: 
   print("bener dikit la")

nilai = int(input("\nmasukkan total anda: "))

if nilai >= 100000:
    print("anda dapat diskon")
else :
    print("maaf, tidak dapat diskon")