# w = int( input("Podaj wiek:") )
# if w > 17:
#     print("Stary cap")
# else:
#     print("Niepełnioletni")
#
def inputGender():
    plec = ''
    while plec == '':
        gender = input('Podaj płeć: (K) - kobieta, (M) - mężczyzna: ')
        if gender == 'K':
            plec = 'K'
        elif gender == 'M':
            plec = 'M'
    return plec
plec = inputGender()
