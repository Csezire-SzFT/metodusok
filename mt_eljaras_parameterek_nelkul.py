# definicio
def koszones():
    print("Jó napot")


def jokivansag():
    print ("Boldog Új Évet!")

def feladat ():
    print("Szeva")
    koszones()
    jokivansag()

def feladat_2 (siker):
    print("Szeva")
    koszones()
    if siker:
        jokivansag()
    else:
        koszones()

# hivás
feladat()

feladat_2(True)


