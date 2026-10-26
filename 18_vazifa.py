shaharlar = {"Toshkent": 3000000, "Farg‘ona": 300000, "Samarqand": 600000}

for shahar, aholi in shaharlar.items():
    if aholi > 500000:
        print(shahar, end=", ")

print("\nEng ko‘p aholi:", max(shaharlar, key=shaharlar.get))