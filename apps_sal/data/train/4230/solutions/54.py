def reverse_letter(string):
    s = ""
    for c in string[::-1]:
        if c.isalpha():
            s += c
    return s
