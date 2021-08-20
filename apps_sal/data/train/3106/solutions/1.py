MAX_BALL = 1 + 800
DP = [[], [0, 1]]
for _ in range(MAX_BALL):
    lst = DP[-1] + [0]
    DP.append([v * i + lst[i - 1] for (i, v) in enumerate(lst)])


def combs_non_empty_boxes(n, k):
    return 'It cannot be possible!' if k > n else DP[n][k]
