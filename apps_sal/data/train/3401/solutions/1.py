from functools import reduce


def getDivisors(n):
    (lst, p) = ([], 2)
    while n > 1:
        while not n % p:
            lst.append(p)
            n //= p
        p += 1 + (p != 2)
    return lst


def eq_dice(diceSet):
    events = reduce(int.__mul__, diceSet)
    lstDivs = getDivisors(events)
    combos = set(genCombDices(tuple(lstDivs), set()))
    return len(combos - {tuple(sorted(diceSet))})


def genCombDices(tup, seens):
    if tup[0] != 2:
        yield tup
    if len(tup) > 2:
        for (i, a) in enumerate(tup):
            for (j, b) in enumerate(tup[i + 1:], i + 1):
                m = a * b
                t = tuple(sorted(tup[:i] + tup[i + 1:j] + tup[j + 1:] + (m,)))
                if m > 20 or t in seens:
                    continue
                seens.add(t)
                yield from genCombDices(t, seens)
