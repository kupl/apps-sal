from itertools import groupby


def _breakdown(word):
    v = sum((c in 'aeiou' for c in word))
    return (v, len(word) - v)


_WORDS = {k: list(group) for (k, group) in groupby(sorted(WORD_LIST, key=_breakdown), key=_breakdown)}


def wanted_words(v, c, forbidden):

    def permitted(word):
        return not any((letter in word for letter in forbidden))
    return filter(permitted, _WORDS.get((v, c), []))
