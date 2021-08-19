def uni_total(string):
    if type(string) != str:
        return 0
    else:
        liste = [ord(i) for i in string]
        return sum(liste)
