def reverse_letter(s):
    a = [i for i in s if i.isalpha()]
    a = ''.join(a)
    return a[::-1]


