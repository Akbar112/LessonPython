jml_match = int(input("Masukkan Jumlah Pertandingan: "))
jml_poin = []
for i in range(jml_match):
    i+=1
    print(f"Poin pertandingan ke-{i}: ", end="")
    poin = int(input())
    poin = jml_poin.append(poin)
print("Total poin adalah:", sum(jml_poin))
print("Rata-rata poin adalah:", sum(jml_poin)/i)