from . import operasi
from . import database

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

    
            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")
    
def update_console():
    read_console()
    while True:
        no_buku = int(input("Masukkan nomor buku : "))
        index_buku = operasi.read(index=no_buku)
        if index_buku:
            break
        else:
            print("")
            
    data_break = index_buku.split(",")
    pk = data_break[0]
    add_date = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]
    
    while True:
        # DISPLAY yang akan diubah
        print("\n"+"="*110)
        print(f"1. Judul \t: {judul:.70}")
        print(f"2. Penulis \t: {penulis:.20}")
        print(f"3. Tahun \t: {tahun:4}")
        print("="*110)
        # User input pilihan yang akan di ubah
        user_option = int(input("Masukkan pilihan (1-3)) : "))
        match(user_option):
            case 1:
                judul = input("Ubah judul : ")
            case 2:
                penulis = input("Ubah penulis : ")
            case 3:
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
                    except:
                        print("tahun harus angka")
            case _:
                print("Error!")
        print("Pembaruan data anda")
        print(f"Judul \t: {judul:.70}")
        print(f"Penulis \t: {penulis:.20}")
        print(f"tahun \t: {tahun:4}")
        isDone = input("Data sudah sesuai (y/n) : ")
        if isDone == 'y' or isDone == 'Y':
            break

    operasi.update(no_buku,pk,add_date,tahun,judul,penulis)
                
    
def create_console():
    judul = input("Judul : ")    
    penulis = input("Penulis :")
    tahun = int(input("Tahun : "))
    
    operasi.create(tahun,judul,penulis)
    print("Data baru ditambahkan!")
    read_console()
    
    
def read_console():
    data_file = operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    '''STYLING'''
    # HEADER
    print("="*110)
    print(f"{index:4} | {judul:70} | {penulis:20} | {tahun:5}")
    print("-"*110)
    # MAIN DATA
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        add_date = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.70} | {penulis:.20} | {tahun:4}\n" , end="")
    # FOOTER
    print("="*110)
    
    
    
    
    
    
    
    
     