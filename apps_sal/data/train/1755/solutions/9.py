def splitlist(x):
    """
    a, b = splitlist(x) finds a partition a, b of x minimizing |sum(a)-sum(b)|
    """
    max_total = sum(x) // 2
    sumset = [{0}]
    for xi in x:
        sumset.append({t + xi for t in sumset[-1] if t + xi <= max_total} | sumset[-1])
    (a, b) = ([], [])
    total = max(sumset[-1])
    for (i, xi) in reversed(list(enumerate(x))):
        if total - xi in sumset[i]:
            a.append(xi)
            total -= xi
        else:
            b.append(xi)
    return (a, b)
