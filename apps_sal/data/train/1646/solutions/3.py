import functools

def automorphic(p):
    t = 1
    n = 5
    k = 1
    res = [1]
    for i in range(1, p + 1):
        size = 2 ** i
        n = (3 * n ** 2 - 2 * n ** 3) % (10 ** size)
        for j in range(k, size + 1):
            m5 = n % (10 ** j)
            m6 = 10 ** j + 1 - m5
            # print("n = " + str(n) + "\n[t, m5, m6] = " + str([t,m5,m6]) + " ")
            res.append(m5)
            res.append(m6)
            # print("res = " + str(res))
    return sorted(list(set(res)))

@functools.lru_cache(maxsize=1)
def greent():
    res = automorphic(13)
    # print(res)
    return res

def green(arg):
    return greent()[arg - 1]
