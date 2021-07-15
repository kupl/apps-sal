import sys


def update(vs, ds, ps, last):
    dec_volume = vs[last]
    dec_hall = 0
    for idx in range(last + 1, len(vs)):
        # already out
        if ps[idx] < 0:
            continue

        # update p: dentist + hall
        ps[idx] -= dec_volume + dec_hall
        if dec_volume > 0:
            dec_volume -= 1
        # child is out, update the hall cry for the next ones
        if ps[idx] < 0:
            dec_hall += ds[idx]


def solve(n, vs, ds, ps):
    cured = []
    for i in range(n):
        if ps[i] < 0:
            continue
        cured.append(i + 1)
        update(vs, ds, ps, i)
    return cured


def __starting_point():
    n = int(next(sys.stdin))
    vs, ds, ps = [[0 for i in range(n)] for x in range(3)]
    for i in range(n):
        line = next(sys.stdin)
        vs[i], ds[i], ps[i] = list(map(int, line.strip().split()))
    cured = solve(n, vs, ds, ps)

    sys.stdout.write(str(len(cured)) + "\n")
    sys.stdout.write(" ".join(map(str, cured)) + "\n")

__starting_point()
