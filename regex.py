import re

a = input("Unesite neki string: ")

b = r'^[Zz][\w\s]*[0-5]+[\s\w]*[bB]$'

c = re.search(b, a)

if b:
    print('Podudara')
else:
    print('Ne podudara')
