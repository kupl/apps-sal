import re


def genMask(w):
    x = list(w)
    for i in range(len(w)):
        x[i] = '.'
        yield ''.join(x)
        x[i] = w[i]


def mutations(alice, bob, word, first):
    players, seen = [alice, bob], {word}
    win, failed, i = -1, -1, first ^ 1
    while 1:
        i ^= 1
        lst = players[i]
        reg = re.compile('|'.join(genMask(word)))
        found = next((w for w in lst if reg.match(w) and w not in seen and len(set(w)) == 4), None)
        if found is None:
            if failed == i ^ 1:
                break
            failed = i
        else:
            seen.add(found)
            word, win = found, i
            if failed != -1:
                break
    return win
