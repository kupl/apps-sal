def best_match(goals1, goals2):
    l = [abs(i - j) for (i, j) in zip(goals1, goals2)]
    ll = [(abs(i - j), j) for (i, j) in zip(goals1, goals2)]
    if l.count(min(l)) > 1:
        l_new = [(a, b) for (a, b) in sorted(ll) if a == min(l)]
        return ll.index(l_new[-1])
    return l.index(min(l))
