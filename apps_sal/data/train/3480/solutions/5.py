def sequence_sum(begin, end, step):
    n = int((end - begin + step)/step)
    an = begin +(n-1) * step
    if step > 0:
        if begin > end:
            return 0
    if step < 0:
        if begin < end:
            return 0
    if n % 2 == 0:
        res = int(int(n/2)*(begin +an))
    if (begin + an) % 2 == 0:
        res = int(int((begin +an)/2)*n)
    return res
