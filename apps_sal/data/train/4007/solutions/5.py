def finding_k(a):
    return next((i for i in range(max(a) - 1, 0, -1) if len(set([j % i for j in a])) == 1), -1)
