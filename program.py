def podaj_wiek():
    wiek = None
    while True:
        w = input("Podaj wiek: ")
        if w.isdigit():
            wiek = int(w)
            if wiek >= 0:
                return wiek
        print("Nieprawidłowy wiek %s. Musi być liczbą całkowitą większą od zera a jest" % (w,))

# if w > 17:
#     print("Stary cap")
# else:
#     print("Niepełnioletni")

wiek = podaj_wiek()
print(wiek)