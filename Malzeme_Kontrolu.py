RECIPE_INGREDIENTS = {"un", "tereyag", "sut", "yumurta", "seker"}

user_input = input("Elinizde bulunan malzemeleri giriniz (virgulle ayirarak): ")
user_ingredients = set(item.strip().lower() for item in user_input.split(", "))

missing_ingredients = RECIPE_INGREDIENTS - user_ingredients
extra_ingredients = user_ingredients - RECIPE_INGREDIENTS

print("\n---Malzeme Kontrol Sonuclari---")
if missing_ingredients:
    print(f"Eksik olan malzemeler sunlardir : {', '.join(missing_ingredients)}")

else:
    print("Tarif icin gerekli olan tum malzemeler elinizde bulunmaktadir")

if extra_ingredients:
    print(f"Elinizde bulunan ekstra malzemeler : {', '.join(extra_ingredients)}")

else:
    print("Elinizde ekstra malzeme bulunmamaktadir")

