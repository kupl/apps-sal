import numpy as np


def pack_bagpack(scores, weights, capacity):
    print(len(scores))
    print(capacity)
    n = len(scores)
    dp = np.zeros((n + 1, capacity + 1))
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= weights[i - 1]:
                dp[i][j] = (max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + scores[i - 1]))
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]
