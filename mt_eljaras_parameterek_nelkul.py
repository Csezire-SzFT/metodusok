# definicio
def koszones():
    print("Jó napot")


def jokivansag():
    print ("Boldog Új Évet!")

def koszones_siman ():
    print("Szeva")
    koszones()
    jokivansag()

def koszones_feltetelekkel (siker):
    koszones()
    if siker:
        jokivansag()
    else:
        koszones()

# hivás
koszones_siman()

koszones_feltetelekkel(True)
