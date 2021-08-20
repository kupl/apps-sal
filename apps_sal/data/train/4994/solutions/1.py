def word_problem(rules, start, to, N):
    q = [(0, 0, start)]
    for (i, n, s) in q:
        if s == to:
            return True
        if n < N and i < len(s):
            q.extend(((i, n + 1, s[:i] + y + s[i + len(x):]) for (x, y) in rules if s[i:].startswith(x)))
            q.append((i + 1, n, s))
    return False
