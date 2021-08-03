def find(d1, d2): return (sum(1for j in d1.values()if len(j) < 2 and "R"not in j), sum(1for j in d2.values()if len(j) < 2 and "R"not in j))


def men_still_standing(a):
    d1 = {i: [] for i in range(1, 12)}
    d2 = __import__("copy").deepcopy(d1)
    for i in a:
        [d1, d2][i[0] == "B"][int(i[1:-1])].append(i[-1])
        r = find(d1, d2)
        if any(j < 7 for j in r):
            return r
    return find(d1, d2)
