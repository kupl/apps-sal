def to_alternating_case(string):
    e = []
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            a = i.lower()
            e.append(a)
        else:
            a = i.upper()
            e.append(a)
    finale = ""
    nuova = finale.join(e)
    return nuova
