def wiek(w):
    if w >= 120:
        print("Otrzymujesz darmowy znicz")
    else:
        print("Czym mogę służyć?")
print(wiek(w))

def aperol(plec, wiek):
    if plec == 'K' and wiek >= 30:
        print("Happy you! Otrzymjesz darmowego aperola")
    else:
        print("Niestety, nie spełniasz kryteriów do otrzymania damarmowego drinka")

def malboro(plec, wiek, region):
    if plec == 'M' and wiek >= 40 and region == 'U':
        print("Gratulacje! Otrzymujesz jedną paczkę papierosów Malboro gratis!")
    else:
        print("Niestety, nie spełniasz kryteriów do otrzymania darmowej paczki papierosów Malboro :(")

def wybierz_region():
    while True:
        region = input("Wybierz region(EUR or USA): ").upper()
        if region == "EUR":
            return "E"
        elif region == "USA":
            return "U"
        else:
            print("Niepoprawny wybór regionu")