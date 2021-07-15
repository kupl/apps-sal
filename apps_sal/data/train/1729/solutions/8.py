def split_path(s):
    while s:
        i = 0
        for c in s:
            if c not in "RLrl":
                break
            i += 1
            yield c
        n = 0
        while i < len(s) and s[i].isdigit():
            n = 10 * n + int(s[i])
            i += 1
        s = s[i:]
        if n:
            yield n


def turn(d, r):
    opt = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    i = opt.index(d) + {"r": 1, "R": 2, "l": -1, "L": -2}[r]
    return opt[i % len(opt)]


def step(p, d, k):
    x, y = p
    dx, dy = d
    return [x + dx * k, y + dy * k]


def i_am_here(path, d={"pos": [0, 0], "dir": [-1, 0]}):
    for p in split_path(path):
        if isinstance(p, int):
            d["pos"] = step(d["pos"], d["dir"], p)
        else:
            d["dir"] = turn(d["dir"], p)
    return d["pos"]
