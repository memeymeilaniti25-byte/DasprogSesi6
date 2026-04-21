while True:
    print("\n-----Menu-----")
    print("1.Hallo")
    print("2.Keluar")

    pilih = input("Masukkan pilihan menu(1/2): ")

    if pilih  == "1":
        print("Halo User")
    elif pilih == "2":
        print("Program berhenti")
        break
    else:
        print("Tidak valid coba lagi")        

