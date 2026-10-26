jamgarma = int(input("Boshlang'ich jamg'arma: "))
haftalik = int(input("Har hafta qo'shiladigan pul: "))
hafta = 0

while jamgarma <= 500000:
    jamgarma += haftalik
    hafta += 1

print(hafta, "hafta kerak")