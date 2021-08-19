import bisect


def s1(n):
    result = 0
    for i in range(1, int(n ** 0.5) + 1):
        (q, r) = divmod(n, i)
        if r == 0:
            result += i
            if q != i:
                result += q
    return result


dup = set()
for i in range(10001):
    ss = str(i)
    rr = ss[::-1]
    if ss >= rr:
        continue
    if s1(i) == s1(int(rr)):
        dup.add(i)
        dup.add(int(rr))
dup = sorted(dup)


def equal_sigma1(nMax):
    return sum(dup[:bisect.bisect(dup, nMax)])
