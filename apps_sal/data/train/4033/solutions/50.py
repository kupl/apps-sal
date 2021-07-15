def contamination(text, char):
    cunt = list(text)
    ctr = 0
    for fuck in cunt:
        cunt[ctr] = char
        ctr += 1
    return ''.join(cunt)
