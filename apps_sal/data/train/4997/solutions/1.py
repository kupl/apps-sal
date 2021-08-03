def sigma1(n):
    ans = 0
    for i in xrange(1, int(n**0.5) + 1):
        if n % i == 0:
            ans += i + n / i
    return ans if n ** 0.5 % 1 != 0 else ans - int(n ** 0.5)


def equal_sigma1(n_max):
    ans = 0
    for i in xrange(528, n_max + 1):
        j = int(str(i)[::-1])
        if i != j and sigma1(i) == sigma1(j):
            ans += i
    return ans
