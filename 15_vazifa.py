birinchi = {"Ali", "Madina", "Jasur", "Aziza"}
ikkinchi = {"Jasur", "Sardor", "Aziza", "Bekzod"}

print("Faqat birinchi:", ", ".join(birinchi - ikkinchi))
print("Faqat ikkinchi:", ", ".join(ikkinchi - birinchi))
print("Ikkalasida:", ", ".join(birinchi & ikkinchi))