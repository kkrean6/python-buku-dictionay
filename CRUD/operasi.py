from . import database
from .util import random_string
import time
import os

def delete(no_buku):
    try:
        with open(database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.rename("data_temp.txt",database.DB_NAME)
      
def update(no_buku,pk,add_date,tahun,judul,penulis):
    mydict = database.TEMPLETE.copy()
    
    mydict["pk"] = pk
    mydict["add_date"] = add_date
    mydict["penulis"] = penulis + database.TEMPLETE["penulis"][len(penulis):]
    mydict["judul"] = judul + database.TEMPLETE["judul"][len(judul):]
    mydict["tahun"] = str(tahun)
    
    data_str = f"{mydict['pk']},{mydict['add_date']},{mydict['judul']},{mydict['penulis']},{mydict['tahun']}\n"
    panjang_data = len(data_str)
    try:
        with open(database.DB_NAME,"r+",encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("")

def create(tahun,judul,penulis):
    mydict = database.TEMPLETE.copy()
    
    mydict["pk"] = random_string(6)
    mydict["add_date"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    mydict["penulis"] = penulis + database.TEMPLETE["penulis"][len(penulis):]
    mydict["judul"] = judul + database.TEMPLETE["judul"][len(judul):]
    mydict["tahun"] = tahun
    
    data_str = f"{mydict['pk']},{mydict['add_date']},{mydict['judul']},{mydict['penulis']},{mydict['tahun']}\n"
    
    try:
        with open(database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("")

def create_data_first():
    judul = input("Judul \t: ")    
    penulis = input("Penulis \t:")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
        except:
            print("tahun harus angka")

    
    mydict = database.TEMPLETE.copy()
    
    mydict["pk"] = random_string(6)
    mydict["add_date"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    mydict["penulis"] = penulis + database.TEMPLETE["penulis"][len(penulis):]
    mydict["judul"] = judul + database.TEMPLETE["judul"][len(judul):]
    mydict["tahun"] = tahun
    
    data_str = f"{mydict['pk']},{mydict['add_date']},{mydict['judul']},{mydict['penulis']},{mydict['tahun']}\n"
    
    try:
        with open(database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("")

    
def read(**kwargs):
    try:
        with open(database.DB_NAME,"r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
                
    except:
        print("")
        return False       
        