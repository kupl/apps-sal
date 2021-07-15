def correct(string):
    l = list(string)
    for idx, char in enumerate(l):
        if char == '5':
            l[idx] = 'S'
        if char == '0':
            l[idx] = 'O'
        if char == '1':
            l[idx] = 'I'
    return ''.join(l)

print(correct("5INGAPORE"))
