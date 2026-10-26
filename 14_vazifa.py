ruxsat = {"matematika", "ingliz", "informatika", "fizika"}
tanlangan = {"ingliz", "informatika", "tarix"}

bor = ruxsat & tanlangan
yoq = tanlangan - ruxsat

print("Ruxsat etilgan:", ", ".join(bor))
print("Ruxsat etilmagan:", ", ".join(yoq))
