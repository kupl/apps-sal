def reverse_letter(string):
    txt = ""
    for a in string:
        if a.isalpha():
            txt = txt + a
    return txt[::-1]


