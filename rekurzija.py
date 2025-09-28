def obrni(s):
    if s == "":
        return ""
    return obrni(s[1:]) + s[0]

a = input("Unesite: ")
print("Obrnuto:", obrni(tekst))
