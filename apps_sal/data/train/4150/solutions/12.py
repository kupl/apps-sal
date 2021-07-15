import string
def rot13(message):
    q = ""
    p = list(string.ascii_lowercase)
    for i in message:
        if i.isalpha()== True:
            a = p.index(i.lower())+ 13
            if i.isupper()== True:
                if a > 25:
                    a -= 26
                q += (p[a]).upper()
            else:
                if a > 25:
                    a -= 26
                q += (p[a]).lower()
        else:
            q += i  
    return q
    

