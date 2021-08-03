def swap(s, n):
    n = str(bin(n))[2:]
    words = list(s)
    binary_mult = str(n) * len(s)
    bn_words = list(binary_mult)
    result = []
    for i, x in enumerate(words):
        if not x.isalpha():
            bn_words.insert(i, x)
        if bn_words[i] == '1':
            result.append(words[i].swapcase())
        else:
            result.append(words[i])
    return ''.join(result)
