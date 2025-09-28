def pozdrav(a):
    return "Pozdrav " + a + "!"


pozdrav1 = lambda a: "Dobrodošao " + a + "!"


def poziv_pozdrav(funkcija):
    a = input("Unesi svoje ime: ")
    print(funkcija(a))


poziv_pozdrav(pozdrav1)
