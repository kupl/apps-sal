from functools import reduce

def splitAlong(xs, ys):
    i = 0
    try:
        while xs[i] == ys[i]:
            i += 1
    except IndexError:
        pass
    return (xs[:i], xs[i:], ys[i:])

def insert(tree, word):
    for key, val in tree.items():
        pref, wt, kt = splitAlong(word, key)
        if pref:
            if kt:
                del tree[key]
                tree[pref] = {wt: {}, kt: val} if wt else {kt: val}
            else:
                insert(tree[pref], wt)
            return tree
    if word:
        tree[word] = {}
    return tree


def radix_tree(*words):
    return reduce(insert, words, {})
