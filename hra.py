import piskvorky

def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka).lower().strip()
        if (odpoved == 'ano') or (odpoved == 'a'):
            return True
        elif (odpoved == 'ne') or (odpoved == 'n'):
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

if ano_nebo_ne('Chceš si zahrát hru? '):
    print(' Zaciname piskvorky ')
    velikost_pole = int(input('Zadej velikost pole: '))
    pole = '-'*velikost_pole
    piskvorky.piskvorky1d(pole)
else:
    print('Škoda.')