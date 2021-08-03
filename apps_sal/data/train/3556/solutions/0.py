from collections import Counter


def diamonds_and_toads(sentence, fairy):
    c = Counter(sentence)
    d = {'good': ['ruby', 'crystal'], 'evil': ['python', 'squirrel']}

    return {s: c[s[0]] + 2 * c[s[0].upper()] for s in d[fairy]}
