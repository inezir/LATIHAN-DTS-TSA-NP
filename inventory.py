# Membuat dictionary kosong
dictionary = {}

# Meminta input "ya" atau "tidak" dari user.
data_lowercase = ""
while data_lowercase != "tidak":
    data = input("Input data Inventory baru (ya/tidak)? ")
    data_lowercase = data.lower()
    print ("*********************************************")
    
    # Meminta input nama perangkat dan lokasi dari user.
    if data_lowercase == "ya":
        file = open ("db-inventory.txt", "a")
        x = (input("Nama Perangkat: "))
        y = (input ("Lokasi: "))
        print ("---------------------------------------------")
    
    # Menyimpan data input ke dalam file "db-inventory.txt"
        file.write("Nama Perangkat: " + x + "\n")
        file.write("Lokasi: " + y + "\n")
        file.close()
        
        # Menyimpan data input nama perangkat dan lokasi ke dictionary.
        dictionary[x] = y
    
    else:
        file.close()
        break

# Menampilkan data-data nama perangkat dan lokasi yang diinput user.
for x, y in dictionary.items ():
    print("Nama Perangkat: ", x, ", Lokasi: ", y)

