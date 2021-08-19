def finding_k(a):
    return max([k for k in range(1, max(a)) if eval('=='.join([str(z) + '%' + str(k) for z in a]))], default=-1)
