import re


def f(name):
    words = re.findall("[\\w']+", name)
    if len(words) == 1:
        return words[0][:4]
    elif len(words) == 2:
        return words[0][:2] + words[1][:2]
    elif len(words) == 3:
        return words[0][:1] + words[1][:1] + words[2][:2]
    return ''.join((word[0] for word in words))


def bird_code(arr):
    return [f(name).upper() for name in arr]
