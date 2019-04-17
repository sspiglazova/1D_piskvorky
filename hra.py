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

def zadej_velikost_pole(otazka):
    while True:
        try:
            velikost_pole = int(input(otazka))
            if velikost_pole < 0:
                raise ArithmeticError('cislo je zaporne')
            return velikost_pole
        except ValueError:
            print('to neni cislo')
        except ArithmeticError:
            print('cislo je zaporne')

if ano_nebo_ne('Chceš si zahrát hru? '):
    print(' Zaciname piskvorky ')
    velikost_pole = zadej_velikost_pole('Zadej velikost pole: ')
    pole = '-' * velikost_pole
    piskvorky.piskvorky1d(pole)
else:
    print('Škoda.')