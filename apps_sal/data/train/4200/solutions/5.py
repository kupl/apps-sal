from itertools import chain
vowel = set("aeiouAEIOU").__contains__


def vowel_shift(text, n):
    if not (text and n):
        return text
    L = list(filter(vowel, text))
    if not L:
        return text
    n %= len(L)
    it = chain(L[-n:], L[:-n])
    return ''.join(next(it) if vowel(c) else c for c in text)
