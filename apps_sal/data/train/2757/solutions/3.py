from re import sub

def check_password(string):
    reduced = sub("[a-z]", "a", sub("[A-Z]", "A", sub("[0-9]", "0", sub("[!@#$%^&*?]", "!", string))))
    return "valid" if 8 <= len(string) <= 20 and set(reduced) == set("aA0!") else "not valid"





## without re
#from string import ascii_lowercase as LOW, ascii_uppercase as UPP, digits as DIG

## without import
#LOW = "abcdefghijklmnopqrstuvwxyz"
#UPP = LOW.upper()
#DIG = "0123456789"

#SPE = "!@#$%^&*?"
#ALLOWED = (LOW, UPP, DIG, SPE)

#def check_password(string):
#    reduced = string.translate(str.maketrans("".join(ALLOWED), "".join(s[0]*len(s) for s in ALLOWED)))
#    return "valid" if 8 <= len(string) <= 20 and set(reduced) == set(s[0] for s in ALLOWED) else "not valid"

