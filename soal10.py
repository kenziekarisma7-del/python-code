usia = int(input("Masukkan usia pengunjung: "))

if usia >= 17:
    print("Pilih genre film:")
    print("1. Horor")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")

    genre = int(input("Pilih genre (1-4): "))

    match genre:
        case 1:
            print("1. Horor Indonesia")
            print("2. Horor Luar Negeri")
            pilihan = int(input("Pilih film: "))
            match pilihan:
                case 1:
                    film = "Horor Indonesia"
                case 2:
                    film = "Horor Luar Negeri"
                case _:
                    film = "Pilihan tidak tersedia"

        case 2:
            print("1. Komedi Indonesia")
            print("2. Komedi Luar Negeri")
            pilihan = int(input("Pilih film: "))
            match pilihan:
                case 1:
                    film = "Komedi Indonesia"
                case 2:
                    film = "Komedi Luar Negeri"
                case _:
                    film = "Pilihan tidak tersedia"

        case 3:
            print("1. Keluarga Indonesia")
            print("2. Keluarga Luar Negeri")
            pilihan = int(input("Pilih film: "))
            match pilihan:
                case 1:
                    film = "Keluarga Indonesia"
                case 2:
                    film = "Keluarga Luar Negeri"
                case _:
                    film = "Pilihan tidak tersedia"

        case 4:
            print("1. Hollywood")
            print("2. Indonesia")
            print("3. Bollywood")
            pilihan = int(input("Pilih film: "))
            match pilihan:
                case 1:
                    film = "Hollywood"
                case 2:
                    film = "Indonesia"
                case 3:
                    film = "Bollywood"
                case _:
                    film = "Pilihan tidak tersedia"

        case _:
            film = "Pilihan tidak tersedia"

else:
    print("Pilih jenis animasi:")
    print("1. Animasi 2 Dimensi")
    print("2. Animasi 3 Dimensi")

    jenis = int(input("Pilih animasi (1-2): "))

    match jenis:
        case 1:
            print("1. Naruto")
            print("2. One Piece")
            pilihan = int(input("Pilih film: "))
            match pilihan:
                case 1:
                    film = "Naruto"
                case 2:
                    film = "One Piece"
                case _:
                    film = "Pilihan tidak tersedia"

        case 2:
            print("1. Nemo")
            print("2. Kungfu Panda")
            pilihan = int(input("Pilih film: "))
            match pilihan:
                case 1:
                    film = "Nemo"
                case 2:
                    film = "Kungfu Panda"
                case _:
                    film = "Pilihan tidak tersedia"

        case _:
            film = "Pilihan tidak tersedia"

if film == "Pilihan tidak tersedia":
    print(film)
else:
    print(f'Selamat Menyaksikan "{film}"')