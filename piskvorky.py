import ai

def vyhodnot(pole):
    if 'xxx' in pole:
        print(pole)
        return 'x'
    elif 'ooo' in pole:
        print(pole)
        return 'o'
    elif '-' not in pole:
        print(pole)
        return '!'
    else:
        return '-'

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace(pole):
    cislo_policka = 0
    while True:
        print('zadej cislo policky')
        cislo_policka = int(input())
        if (cislo_policka >= 0) and (cislo_policka <= 19) and (pole[cislo_policka] == '-'):
            return tah(pole, cislo_policka, 'x')
        else:
            print('bud pole je obsazeno nebo cislo je zaporne nebo prilis velke')

def piskvorky1d():
        pole = '-'*20
        while '-' in pole:
            print(pole)
            pole = tah_hrace(pole)
            pole = tah_pocitace(pole)
            result = vyhodnot(pole)
            if result != '-':
                print(result)
                break