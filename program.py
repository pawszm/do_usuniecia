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
    region = ""
    while region == "":
        region_tmp = input("Wybierz region(EUR or USA): ").upper()
        if region_tmp == "EUR":
            region = "E"
        elif region_tmp == "USA":
            region = "U"
        else:
            print("Niepoprawny wybór regionu")
    return region


wiek_os = podaj_wiek()
plec = inputGender()
region = wybierz_region()

if (wiek_os >= 18 and region == "E") or (wiek_os >= 21 and region == "U"):
    print("Sprzedajemy alkohol")
    wiek(wiek_os)
    aperol(plec, wiek_os)
    malboro(plec, wiek_os, region)
else:
    print("Osoba niepełnoletnia nie sprzedajemy")
