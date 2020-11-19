color = input("Masukkan warna lampu: ")
if color == "merah":
    jarak = int(input("Masukkan jarak persembunyian: "))
    if jarak >= 5:
        print("Baik, mari kita ke tempat persembunyian dengan motor")
    elif jarak <= 5:
        print("Baik, mari kita ke tempat persembunyian dengan jalan kaki saja")
elif color == "hijau":
    jml_musuh = int(input("Masukkan jumlah musuh: ")) 
    if jml_musuh >= 5:
        print("Okey, kita serang musuh dengan granat")
    elif jml_musuh <= 5:
        print("Okey, kita serang musuh cukup dengan pisau saja")
