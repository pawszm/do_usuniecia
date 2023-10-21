

wybor_plci = ['K', 'M']
plec = input("Podaj swoja plec: ")
wiek = input("Podaj swoj wiek: ")
region = input("Podaj region: ")
wiek = int(wiek)

def aperol():
    if plec == 'K' and wiek == 30:
        print("Happy you! Otrzymjesz darmowego aperola")
    else:
        print("Niestety, nie spełniasz kryteriów do otrzymania damarmowego drinka")

def malboro():
    if plec == 'M' and wiek >= 40 and region == 'U':
        print("Gratulacje! Otrzymujesz jedną paczkę papierosów Malboro gratis!")
    else:
        print("Niestety, nie spełniasz kryteriów do otrzymania darmowej paczki papierosów Malboro :(")

print(aperol())
print(malboro())










