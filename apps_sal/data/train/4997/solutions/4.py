n = 100000

s = list(range(1, n+2))

for d in range(2, int(n**.5) + 1):
    for i in range(d*d, n+1, d):
        s[i] += d
        s[i] += i//d
    s[d*d] -= d

def equal_sigma1(n):
    return sum(x for x in range(n+1)
        if str(x) != str(x)[::-1] and s[x] == s[int(str(x)[::-1])])
