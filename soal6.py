bulan = int(input("pilih bulan 1-6: "))

match bulan:
    case 1: 
        print("JANUARI")
    case 2:
        print("FEBRUARI")
    case 3:
        print("MARET")
    case 4:
        print("APRIL")   
    case 5:
        print("MEI")
    case 6:
        print("JUNI")
    case _:
        print("BULAN ANDA TIDAK TERSEDIA!")