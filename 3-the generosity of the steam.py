member = input("Apakah member? ")
time = int(input("Lama member (tahun)? "))
month = input("Bulan lahir? ")
year = int(input("Tahun game? "))
multi = input("Apakah multiplayer? ")
skema1 = 0
skema2 = 0

if member in ("Ya", "ya", "YA"):
    skema1 += 5
if time <= 10 and time >= 5 :
    skema1 += 20
else :
    skema1 += 30
if month in ("November", "november", "NOVEMBER"):
    skema1 += 20

if year < 2010  :
    skema2 += 40
if multi in ("Ya", "ya", "YA"):
    skema2 += 10

if skema1 > skema2 :
    print(f'Jumlah diskon maksimal adalah: {skema1}% melalui gabungan diskon Skema 1')
else :
    print(f'Jumlah diskon maksimal adalah: {skema2}% melalui gabungan diskon Skema 2')