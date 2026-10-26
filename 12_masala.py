kodlar = ["A12", "B15", "A12", "C20", "B15", "D10"]

noyob = list(dict.fromkeys(kodlar))

print("Noyob kodlar soni:", len(noyob))
print("Kodlar:", ", ".join(noyob))