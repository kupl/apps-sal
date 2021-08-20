from collections import Counter


def remove_duplicate_words(strr):
    input = strr.split(' ')
    for i in range(0, len(input)):
        input[i] = ''.join(input[i])
    UniqW = Counter(input)
    s = ' '.join(UniqW.keys())
    return s
