from collections import Counter


def freq_seq(s, sep):
    dic = Counter(s)
    result = ''

    for char in s:
        for key, value in list(dic.items()):
            if char == key:
                result += str(value) + sep

    return result[:-1]
