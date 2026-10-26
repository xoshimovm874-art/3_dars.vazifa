harorat = (18, 20, 17, 23, 25, 21, 19)

natija = [x for x in harorat if x > 20]

print("Haroratlar:", *natija, sep=" ")
print("Kunlar soni:", len(natija))