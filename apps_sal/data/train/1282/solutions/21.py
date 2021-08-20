t = int(input())
m = 10 ** 9 + 7
while t:
    p = 0
    res = 0
    (l, r) = map(int, input().split())
    d = r - l + 1
    br = bin(r)[2:]
    lbr = len(br)
    l = bin(l)[2:]
    k = -1
    lol = 0
    ll = len(l)
    ind = ll - 1
    if 2 ** ll > r:
        for i in range(ll):
            if l[i] == '0' and br[i] == '1':
                ind = i
                break
        for i in range(len(l) - 1, ind, -1):
            k += 1
            if l[i] == '1':
                a = 2 ** k
                p += a
                res += (min(r + 1, 2 ** (k + 1)) - p) * a
        for i in range(ind + 1):
            if l[i] == '1':
                res += 2 ** (ll - i - 1) * d
    else:
        for i in range(len(l) - 1, -1, -1):
            k += 1
            if l[i] == '1':
                a = 2 ** k
                p += a
                res += (min(r + 1, 2 ** (k + 1)) - p) * a
    print(res % m)
    t -= 1
