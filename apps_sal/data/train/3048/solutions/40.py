def alternateCase(s):
    a = ""
    for x in s:
        if x.isupper():
            a += x.lower()
        elif x.islower():
            a += x.upper()
        elif x == " ":
            a += " "
    return a
