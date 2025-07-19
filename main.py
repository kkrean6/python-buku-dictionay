import os
import CRUD as CRUD
import CRUD.operasi

if __name__ == "__main__" :
    operation_system = os.name

        
    while True:

        match(operation_system):
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")


        print("="*50)
        print(" "*20,"DATABASE BUKU"," "*20)
        print("="*50)
        print("\n1. Read\n2. Add Data\n3. Update Data\n4. Delete Data\n")

        try:
            CRUD.init_console()
            option = int(input("Masukkan pilihan : "))
            if 1 <= option <= 4:    
                True
            else:
                print("Harus 1-4!")
        except:
            print("Perintah tidak ada!")   

        match(option):
            case 1: 
                CRUD.read_console()
            case 2: 
                CRUD.create_console()
            case 3: 
                CRUD.update_console()
            case 4: 
                CRUD.delete_console()
            
        isDone = input("Lanjutkan (y/n) : ")
        if isDone == 'n' or isDone == 'N':
            break
        
    print("Program selesai!")
   