def encrypt(text, key):
    import numpy as np
    import string

    mapowanie_dig_str = dict(zip([x for x in range(0, 26)], list(string.ascii_uppercase)))
    mapowanie_str_dig = dict(zip(list(string.ascii_uppercase), [x for x in range(0, 26)]))

    l_key = []
    for s in key.upper():
        l_key = l_key + [mapowanie_str_dig[s]]

    key_array_dig = np.array([l_key[0:2], l_key[2:]])
    correct_text = ''
    for s in text.upper():
        if s in string.ascii_uppercase:
            correct_text = correct_text + s

    if len(correct_text) % 2 != 0:
        correct_text = correct_text + 'Z'

    output = ''
    l_core = list(correct_text)
    while l_core != []:
        pice_text_array = np.array([[mapowanie_str_dig[l_core[0]]], [mapowanie_str_dig[l_core[1]]]])
        l_core.pop(0)
        l_core.pop(0)
        P = (key_array_dig.dot(pice_text_array)) % 26
        output = output + mapowanie_dig_str[P[0][0]] + mapowanie_dig_str[P[1][0]]

    return output
