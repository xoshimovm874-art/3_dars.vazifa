ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}

print("Eng ko'p:", max(ombor, key=ombor.get), f"({max(ombor.values())} ta)")
print("Eng kam:", min(ombor, key=ombor.get), f"({min(ombor.values())} ta)")
print("Jami mahsulot:", sum(ombor.values()), "ta")