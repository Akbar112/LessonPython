hari = 0
suhu = False
while (not suhu):
    hari += 1
    temp = float(input(f"Masukkan suhu tubuh hari ke-{hari}: "))
    if temp <= 37.2 and temp >= 36.5:
        print("Suhu tubuh sudah normal, pengobatan selesai, terima kasih.")
        suhu = True
    elif temp > 37.2:
        print("Anda harus makan obat demam")
        suhu = False
    elif temp < 36.5:
        print("Anda harus makan obat hipotermia")
        suhu = False