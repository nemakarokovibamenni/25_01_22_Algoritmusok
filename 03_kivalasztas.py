'''
A KIVÁLASZTÁS esetében azt tudjuk, hogy szerepel (legalább) egy bizonyos tulajdonságú elem 
az adatsorban (itt a listában), és ennek az elemnek az indexére vagyunk kíváncsiak.

A program azt vizsgálja, hogy hányadik indexű helyen áll a hárommal osztható szám a listában. 
Az első ilyen elem előfordulása érdekel bennünket.  
'''
szamok = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
for index in range(len(szamok)):
        if szamok[index] % 3 == 0:
            talalat = True
            break

if talalat == True:
    print('A hárommal osztható szám indexe a listában: ', index-1)
else:
    print('Nincs a listában 3-mal osztható szám')