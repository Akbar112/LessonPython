jml_poin = 0
jml_match = int(input("Masukkan Jumlah Pertandingan: "))
for i in range(jml_match):
    i += 1
    poin = input(f"Poin pertandingan ke-{i} : ")
    if poin == "W":
         jml_poin += 3
    elif poin == "D":
         jml_poin += 1
    elif poin == "L":
         jml_poin += 0
    avg = jml_poin / jml_match
print(f"Total poin adalah: {jml_poin}")
print(f"Rata-rata poin adalah: {avg}")
    