import random

szam = random.randint(1, 100)
tipp = int(input('Írj be egy számot 1 és 100 között: '))

while tipp != szam:
    if tipp > szam:
        print('Túl magas!')
    else:
        print('Túl alacsony')
    tipp = int(input('Írj be egy számot 1 és 100 között: '))

print(f'Gratulálok, eltaláltad! A szám {szam} volt. ')