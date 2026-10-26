jami = 0
soni = 0

while True:
    xarajat = int(input())

    if xarajat == 0:
        break

    jami += xarajat
    soni += 1

print("Jami:", jami)
print("Kiritilgan xarajatlar soni:", soni)

if soni > 0:
    print("O'rtacha:", round(jami / soni, 2))
else:
    print("O'rtacha: 0")