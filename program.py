w = input("Podaj wiek: ")
w=int(w)

def wiek(w):
    if w >= 120:
        print("Otrzymujesz darmowy znicz")
    else:
        print("Czym mogę służyć?")
print(wiek(w))

