def reverse_letter(string):
    str = ''
    for n in string:
        if n.isalpha():
            str = n + str
    return str
