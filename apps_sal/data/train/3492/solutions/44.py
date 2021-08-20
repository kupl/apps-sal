def correct_polish_letters(st):
    new_string = ''
    eng = 'acelnoszz'
    pol = 'ąćęłńóśźż'
    for i in range(len(st)):
        if st[i] in pol:
            new_string += eng[pol.index(st[i])]
        else:
            new_string += st[i]
    return new_string
