def podaj_wiek():
    wiek = None
    while True:
        w = input("Podaj wiek: ")
        if w.isdigit():
            wiek = int(w)
            if wiek >= 0:
                return wiek
        print(
            "Nieprawidłowy wiek %s. Musi być liczbą całkowitą większą od zera a jest"
            % (w,)
        )


def inputGender():
    plec = ""
    while plec == "":
        gender = input("Podaj płeć: (K) - kobieta, (M) - mężczyzna: ")
        if gender == "K":
            plec = "K"
        elif gender == "M":
            plec = "M"
    return plec


def wiek(w):
    if w >= 120:
        print("Otrzymujesz darmowy znicz")
    else:
        print("Czym mogę służyć?")


def aperol(plec, wiek):
    if plec == "K" and wiek >= 30:
        print("Happy you! Otrzymjesz darmowego aperola")
    else:
        print("Niestety, nie spełniasz kryteriów do otrzymania damarmowego drinka")


def malboro(plec, wiek, region):
    if plec == "M" and wiek >= 40 and region == "U":
        print("Gratulacje! Otrzymujesz jedną paczkę papierosów Malboro gratis!")
    else:
        print(
            "Niestety, nie spełniasz kryteriów do otrzymania darmowej paczki papierosów Malboro :("
        )


def wybierz_region():
    while True:
        region = input("Wybierz region(EUR or USA): ").upper()
        if region == "EUR":
            return "E"
        elif region == "USA":
            return "U"
        else:
            print("Niepoprawny wybór regionu")
