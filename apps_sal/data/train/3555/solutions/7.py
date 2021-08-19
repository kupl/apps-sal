def hanoi(n, a, b):
    if n == 1:
        return [(a, b)]
    else:
        c = 3 - a - b
        return hanoi(n - 1, a, c) + [(a, b)] + hanoi(n - 1, c, b)


def hanoiArray(n):
    moves = hanoi(n, 0, 2)
    towers = [list(range(n, 0, -1)), [], []]
    ans = [str(towers)]
    for (i, j) in moves:
        towers[j].append(towers[i].pop())
        ans.append(str(towers))
    return '\n'.join(ans)
