# menu utama
jadwal_matkul = []
while True:
    print("=== menu ===")
    print("-CREAT")
    print("-READ")
    print("-DELETE")
    print("-LOGOUT")

    pilih = input("pilih menu: ")
# menu CREAT
    if pilih == "CREAT":    
        while True:
            jawab = input("apakah anda ingin menambahkan jadwal matkul? (yes/no):")
# menambahkan jadwal matkul  
            if jawab == "yes":
                nama_matkul = input("masukan nama matkul:")
                hari = input("masukan hari:")
                jam = input("masukan jam:")
                nama_gedung = input("masukan nama gedung:")
            
                jadwal_matkul.append([nama_matkul, hari, jam, nama_gedung])

                print("data berhasil di tambahkan")

            elif jawab == "no":
                print("penambahan jadwal matkul selesai")
                break
            else:
                print("jawaban tidak valid silahkan jawab yes/no")

# menu READ          
    elif pilih == "READ":
            if jadwal_matkul == "":
                print("jadwal mata kuliah belum di tambahkan.")
# menampilkan semua jadwal matkul
            else:
                print("==daftar jadwal matkul==")
                for matkul in jadwal_matkul:
                    print("nama matkul  :", matkul[0])
                    print("hari         :", matkul[1])
                    print("jam          :", matkul[2])
                    print("nama gedung  :", matkul[3])
                    print()

# menu DELETE
    elif pilih == "DELETE":
        if not jadwal_matkul :
            print("jadwal mata kuliah belum di tambahkan")
# mencari nama matkul yang ingin di hapus
        else:            
            cari_matkul_hapus = input("masukan nama matkul yang ingin di hapus: ")  

            for matkul in jadwal_matkul:
                 if matkul[0] == cari_matkul_hapus:
                      print(f"data jadwal di temukan: {matkul}")
# menyakinkan apakah setuju untuk menghapus data 
                      jawab = input("apakah anda ingin menghapus data? yes/no: ")

                      if jawab == "yes":
                        jadwal_matkul.remove(matkul)
                        print(f"data jadwal matkul dengan nama_matkul {cari_matkul_hapus} berhasil di hapus")
                      elif jawab == "no": 
                        print("data jadwal matkul tidak di hapus")
                      break
                 else:
                    print("jawaban tidak valid silahkan jawab yes/no")

                 break   
            else:
                print("data nama mata kuliah tidak ditemukan")  

# menu LOGOUT jika ingin keluar
    elif pilih == "LOGOUT":
         print("anda berhasil keluar. program selesai")    
         break

    else:
         print("pilihan tidak valid")    