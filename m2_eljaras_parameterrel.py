# definició, nélküle nem lehet hívni metódust
# lokális változóval
def koszones_1():
    nev = "Péter" #lokális változó, ez elfedi a globálisan (fő modulban megadottat),
    # ezért a paraméterben megadott változó sem használható lokális változóként
    print (f"Szeva {nev}!")


def koszones_2(nev):
    print (f"Szeva {nev}!")


def duplaz(szam):
    print (f"A szám: {szam}, a duplája: {szam*2}!")



# hívás
print("Szeva")

koszones_1()

koszones_2("Sanyi")

duplaz (5)


