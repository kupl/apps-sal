from operator import itemgetter
from numpy import delete


def make_spanning_tree(edges, t):
    memo, result = [], []
    for v in sorted(edges, key=itemgetter(1), reverse=(t == "max")):
        (x, y), w = v

        if x == y:
            continue

        i = next((i for i, s in enumerate(memo) if x in s), None)
        j = next((j for j, s in enumerate(memo) if y in s), None)

        if i == j != None:
            continue

        result.append(v)

        if i == j:
            memo.append({x, y})
        elif i is None:
            memo[j].add(x)
        elif j is None:
            memo[i].add(y)
        else:
            memo.append(memo[i] | memo[j])
            memo = delete(memo, [i, j]).tolist()

    return result
