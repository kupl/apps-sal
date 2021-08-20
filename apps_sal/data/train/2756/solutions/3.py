def search_permMult(nMax, k):

    def tod(n):
        return ''.join(sorted([d for d in str(n)]))
    i = 1
    cnt = 0
    while i <= nMax // k:
        if tod(i) == tod(i * k):
            cnt += 1
        i += 1
    return cnt
