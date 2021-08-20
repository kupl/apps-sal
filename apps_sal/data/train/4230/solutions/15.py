def reverse_letter(string):
    a = []
    for i in string:
        if i.isalpha():
            a.append(i)
    return ''.join(list(reversed(a)))
