def podaj_wiek():
    wiek = None
    while True:
        w = input("Podaj wiek: ")
        if w.isdigit():
            wiek = int(w)
            if wiek >= 0:
                return wiek
        print("Nieprawidłowy wiek %s. Musi być liczbą całkowitą większą lub równą zero a jest" % (w,))

def inputGender():
    plec = ''
    while plec == '':
        gender = input('Podaj płeć: (K) - kobieta, (M) - mężczyzna: ')
        if gender == 'K':
            plec = 'K'
        elif gender == 'M':
            plec = 'M'
    return plec
  
def wiek(w):
    if w >= 120:
        print("Otrzymujesz darmowy znicz")

def aperol(plec, wiek):
    if plec == 'K' and wiek >= 30 and wiek < 120:
        print("Happy you! Otrzymjesz darmowego aperola")

def malboro(plec, wiek, region):
    if plec == 'M' and wiek >= 40 and wiek < 120 and region == 'U':
        print("Gratulacje! Otrzymujesz jedną paczkę papierosów Malboro gratis!")

def wybierz_region():
    while True:
        region = input("Wybierz region(EUR or USA): ").upper()
        if region == "EUR":
            return "E"
        elif region == "USA":
            return "U"
        else:
            print("Niepoprawny wybór regionu")

wiek_os = podaj_wiek()
plec = inputGender()
region = wybierz_region()

if (wiek_os >= 18 and region == "E") or (wiek_os >= 21  and region == "U"):
    print("Sprzedajemy alkohol")
    wiek(wiek_os)
    aperol(plec,wiek_os)
    malboro(plec,wiek_os,region)
else:
    print("Osoba niepełnoletnia - nie możemy sprzedać alkoholu")
