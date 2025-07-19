from . import operasi

DB_NAME = "data.txt"
TEMPLETE = {
    "pk" : "XXXXXX",
    "add_date" : "yyyy-mm-dd",
    "judul" : 255*" ",
    "penulis" : 255*" ",
    "tahun" : "yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("\nData buku tersedia!\n")
        
    except:
        print("\nData tidak tersedia! Membuat file baru!")
        operasi.create_data_first()