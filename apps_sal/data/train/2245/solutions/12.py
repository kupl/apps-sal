def solve():
    (n, m, k) = list(map(int, input().strip().split()))
    array = list(map(int, input().strip().split()))
    ops = [tuple(map(int, input().strip().split())) for _ in range(m)]
    applied = [0 for _ in range(m + 1)]
    qs = [tuple(map(int, input().strip().split())) for _ in range(k)]
    for (x, y) in qs:
        applied[x - 1] += 1
        applied[y] -= 1
    cumadds = [0 for _ in range(n + 1)]
    repeats = 0
    for (i, (l, r, d)) in enumerate(ops):
        repeats += applied[i]
        cumadds[l - 1] += repeats * d
        cumadds[r] -= repeats * d
    cum = 0
    for (i, cumadd) in zip(list(range(n)), cumadds):
        cum += cumadd
        array[i] += cum
    print(*array)


solve()
