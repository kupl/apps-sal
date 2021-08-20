def leaderboard_climb(A, K):
    return (lambda S: [len(S) - __import__('bisect').bisect(S, i) + 1 for i in K])(sorted(set(A)))
