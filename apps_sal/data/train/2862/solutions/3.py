def leaderboard_climb(A, K): return (lambda S: [len(S) - __import__('bisect').bisect(S, i) + 1for i in K])(sorted(set(A)))
