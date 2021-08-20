def vowel_2_index(string):
    vowels = 'aAeEiIoOuU'
    r = []
    for (i, item) in enumerate(string, 1):
        if item not in vowels:
            r.append(item)
        else:
            r.append(str(i))
    return ''.join(r)
