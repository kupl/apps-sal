from itertools import groupby
tr = [(0,), ('b', 'f', 'p', 'v'), ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'), ('d', 't'), 'l', ('m', 'n'), 'r']


def soundex(name):
    name = name.lower().split(' ')
    first_l = [e[0].upper() for e in name]
    let_to_dig = loop(lambda x: indx(x, tr), loop(lambda x: x, name, lambda x: x not in 'hw'))
    del_duble = loop(lambda x: x[0], let_to_dig, funk2=lambda x: groupby(x))
    del_vowel = [[e[0], ''.join([x for (i, x) in enumerate(e) if x.isdigit() and i])] for e in del_duble]
    return ' '.join((([first_l[i], e[0].upper()][all((e[0].isalpha(), e[0] == first_l[i]))] + ['', e[0]][all((e[0].isdigit(), first_l[i] in 'HW'))] + e[1]).ljust(4, '0')[:4] for (i, e) in enumerate(del_vowel)))


def indx(elem, arr):
    for (i, x) in enumerate(arr):
        if elem in x:
            return str(i)
    return elem


def loop(func1, arr, excuse1=lambda x: x, excuse2=lambda x: x, funk2=lambda x: x):
    return [[func1(x) for x in funk2(e) if excuse1(x)] for e in arr if excuse2(e)]
