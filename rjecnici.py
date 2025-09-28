import random

imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra',
         'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena',
         'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija',
         'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana',
         'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

ocjene = {}
for ime in imena:
    ocjena = random.randint(1, 5)
    ocjene[ime] = ocjena


brojac = {}
for ocjena in ocjene.values():
    if ocjena in brojac:
        brojac[ocjena] += 1
    else:
        brojac[ocjena] = 1


print("Broj ocjena:")
for ocjena in sorted(brojac.keys()):
    print(ocjena, "=", brojac[ocjena])


a = len(ocjene)
polozili = 0
for ocjena in ocjene.values():
    if ocjena > 1:
        polozili += 1

postotak = polozili / a * 100
print("Postotak:", postotak, "%")
