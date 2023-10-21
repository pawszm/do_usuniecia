w = int(input("Podaj wiek:"))


def wybierz_region():
    while True:
        region = input("Wybierz region(EUR or USA): ").upper()
        if region == "EUR":
            return "E"
        elif region == "USA":
            return "U"
        else:
            print("Niepoprawny wybór regionu")


region = wybierz_region()
print("wybrany region: ", region)

if w > 17:
    print("Stary cap")
else:
    print("Niepełnioletni")
