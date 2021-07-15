def prefix1(a, b):
    cnt = 0
    for i, j in zip(a, b):
        if i == j:
            cnt += 1
        else:
            return cnt
    return cnt    
def prefix2(a, b, num):
    for i in range(num, -1, -1):
        if b.startswith(a[:i]):
            return i
def zfunc(str_):
    z = []
    k = len(str_)
    for i in range(len(str_)):
        z.append(prefix2(str_[i:], str_[: k - i], k - i))
        #z.append(prefix1(str_[i:], str_[: k - i]))     #poor timing
    return z
