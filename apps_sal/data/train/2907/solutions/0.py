MAX_BALL = 2 + 1800
(DP, lst) = ([None], [0, 1])
for _ in range(MAX_BALL):
    DP.append([sum(lst), *max(((v, i) for (i, v) in enumerate(lst)))])
    lst.append(0)
    lst = [v * i + lst[i - 1] for (i, v) in enumerate(lst)]
combs_non_empty_boxesII = DP.__getitem__
