def hofstadter_Q(n):
    q = [1, 1]
    while len(q) < n:
        q.append(q[-q[-1]] + q[-q[-2]])
    return q[-1]
