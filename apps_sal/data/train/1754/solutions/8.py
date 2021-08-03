from itertools import combinations


def valid(s):
    all_char = sorted(list(set([k for i in s for j in i for k in j])))
    c, c1, store = [], [], []
    for i in s:
        c.append(all_char == sorted("".join(i)))
        for j in i:
            c1.append(len(j) + len(i))
            for k in combinations(j, 2):
                if k in store:
                    return False
                store.append(k)
    return all(c) and len(set(c1)) < 2
