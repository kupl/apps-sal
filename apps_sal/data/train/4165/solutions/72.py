def uni_total(string):
    # your code here
    rez = 0
    for c in string:
        rez += ord(c)
    return rez
