def is_substitution_cipher(s1, s2):
    dict1 = {}
    dict2 = {}
    for i, j in zip(s1, s2):
        dict1[i] = dict1.get(i, 0) + 1
        dict2[j] = dict2.get(j, 0) + 1
        if len(dict1) != len(dict2):
            return False
    return True
