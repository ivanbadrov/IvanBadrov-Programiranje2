import re

e_mail = input("Unesi e-mail: ").lower()
edu_id = input("Unesi eduID: ").lower()


regex_e_mail = r'^[a-zčćžšđ]+\.{1}[a-zčćžšđ]+@fpmoz\.sum\.ba$'

regex_edu_id = r'^[a-zčćžšđ]{1}[a-zčćžšđ]+[0-9]*@sum\.ba$'

if re.fullmatch(regex_e_mail, e_mail):
    print("E-mail je ispravan")
else:
    print("E-mail nije ispravan")

if re.fullmatch(regex_edu_id, edu_id):
    print("eduID je ispravan")
else:
    print("eduID nije ispravan")
