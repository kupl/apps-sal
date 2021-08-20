def allmult(n):
    l = list(range(2, n))
    l = l[:len(l) // 2 + 1]
    m = set()
    for (i, n1) in enumerate(l):
        for n2 in l[i:]:
            if n1 * n2 == n:
                m.add((n1, n2))
    return m


def addPart(n, s):
    news = set()
    for t in s:
        newt = tuple(sorted(t + (n,)))
        news.add(newt)
    return news


def is_mult(l, num):
    m = 1
    for n in l:
        m *= n
    return m == num


def lastPart(newpart, n):
    lastpart = newpart.copy()
    for nums in newpart:
        nums = list(nums)
        great = max(nums)
        nums.remove(great)
        for mult in map(list, allmult(great)):
            mult.extend(nums)
            part = tuple(sorted(mult))
            if is_mult(part, n):
                lastpart.add(part)
    return lastpart


def prod_int_part(n):
    part = allmult(n)
    newpart = part
    for (n1, n2) in part:
        newpart = newpart.union(addPart(n1, allmult(n2)))
        newpart = newpart.union(addPart(n2, allmult(n1)))
    lastpart = lastPart(lastPart(newpart, n), n)
    return [len(lastpart), list(max(lastpart, key=len))] if lastpart else [0, []]
