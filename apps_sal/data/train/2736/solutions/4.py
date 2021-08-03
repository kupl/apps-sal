from itertools import permutations, groupby


def largest_arrangement(a):
    a = sorted(a, key=lambda x: str(x)[0])[::-1]
    t = ''
    for i, j in groupby(a, key=lambda x: str(x)[0]):
        li = []
        for k in permutations(list(j)):
            li.append(int("".join(map(str, k))))
        t += str(max(li))
    return int(t)
