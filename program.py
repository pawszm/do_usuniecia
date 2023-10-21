w = input("Podaj wiek: ")
w=int(w)

def wiek(w):
    if w >= 120:
        print("Takich dziadów nie obsługujemy")
    else:
        print("Czym mogę służyć?")
print(wiek(w))

