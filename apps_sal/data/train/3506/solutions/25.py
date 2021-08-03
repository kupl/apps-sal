def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    ret = []
    ind = 1
    for z in word:
        if z.lower() in vowels:
            ret.append(ind)
        ind += 1
    return ret
