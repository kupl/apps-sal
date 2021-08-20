def sumDig_nthTerm(base, cycle, k):
    (loop, remaining) = divmod(k - 1, len(cycle))
    term = base + loop * sum(cycle) + sum(cycle[:remaining])
    return sum((int(d) for d in str(term)))
