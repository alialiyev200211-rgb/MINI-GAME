import random
"""
27.04.2026 yil
Mavzu: Pythonda grafika bilan ishlash
(SONNI TOP O'YINI YARATISH)
"""

print("SONNI TOP O'YINI (1-1000)")
print("\n1-bosqich: Siz son topasiz")

son = random.randint(1, 1000)
user_urunish = 0

while True:
    taxmin = int(input("Taxmin kiriting (1-1000): "))
    user_urunish += 1
    if taxmin < son:
        print("O'ylagan sonim bundan kattaroq")
    elif taxmin > son:
        print("O'ylagan sonim bundan kichikroq")
    else:
        print(f"Topdingiz! Urunishlar: {user_urunish}")
        break
# ikkinchi bosqich
print("\n2-bosqich: Kompyuter son topadi")
print("1 dan 1000 gacha son o'ylang! ")
past = 1
yuqori = 1000
komp_urunish = 0

while True:
    taxmin = (past + yuqori)//2
    komp_urunish += 1
    print(f"Kompyuter taxmini: {taxmin}")
    javob = input("To'g'rimi (=), katta (+), kichik (-): ")
    if javob == "=":
        print(f"Kompyuter topti! Urunishlar: {komp_urunish}")
        break
    elif javob == "+":
        past = taxmin + 1
    elif javob == "-":
        yuqori = taxmin - 1
    else:
        print("Noto'gri belgi !")

print("\nNatijalar:")
print(f"Siz: {user_urunish} ta urunish")
print(f"Kompyuter: {komp_urunish} ta urunish")
if user_urunish<komp_urunish:
    print("SIZ YUTDINGIZ !")
elif user_urunish>komp_urunish:
    print("KOMPYUTER YUTDI!")
else:
    print("DURRANG !")

