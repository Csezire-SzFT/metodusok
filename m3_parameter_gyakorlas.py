def kerulet(a, b):
    return "A kerület " + str(2 * (a + b)) + " (a: " + str(a) + ", b: " + str(b) + ")"


def terulet (a, b):
    return "A terület " + str(a * b) + " (a: " + str(a) + ", b: " + str(b) + ")"


def terulet_es_kerulet (a_oldal: float, b_oldal: float):
    return kerulet(a_oldal, b_oldal) + " " + str(terulet(a_oldal, b_oldal))


print(terulet_es_kerulet(5, 8))
print(terulet(13, 6))
print(kerulet(23, 18))




