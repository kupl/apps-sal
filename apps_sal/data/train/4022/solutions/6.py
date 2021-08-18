CONS_VAL = {
    'b': '1', 'f': '1', 'p': '1', 'v': '1', 'c': '2', 'g': '2',
    'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
    'd': '3', 't': '3', 'l': '4', 'm': '5', 'n': '5', 'r': '6'}


def soundex(name):
    result = []

    for word in name.lower().split():
        first = word[0]

        word = [first] + [c for c in word[1:] if c not in 'hw']

        word = [CONS_VAL.get(c, c) for c in word]

        word = [first] + [c for i, c in enumerate(word[1:]) if word[i] != c]

        word = [first] + [c for c in word[1:] if c not in 'aeiouy']

        word = (word + ['0'] * 3)[:4]
        result.append(''.join(word))

    return ' '.join(result).upper()
