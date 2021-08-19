def conjugate(verb):
    i = 0
    conj = ''
    while i < len(verb) - 2:
        conj += verb[i]
        i += 1
    arr = []
    vow = verb[-2]
    arr.append(conj + 'o')
    if vow == 'a':
        arr.append(conj + 'as')
        arr.append(conj + 'a')
    else:
        arr.append(conj + 'es')
        arr.append(conj + 'e')
    if vow == 'a':
        arr.append(conj + 'amos')
        arr.append(conj + 'ais')
        arr.append(conj + 'an')
    elif vow == 'e':
        arr.append(conj + 'emos')
        arr.append(conj + 'eis')
        arr.append(conj + 'en')
    else:
        arr.append(conj + 'imos')
        arr.append(conj + 'is')
        arr.append(conj + 'en')
    obj = {verb: arr}
    return obj
