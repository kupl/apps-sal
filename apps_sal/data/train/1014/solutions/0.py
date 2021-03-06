from math import log2, ceil
MOD = int(1000000000.0 + 7)


def srt(s):
    return ''.join(sorted(s))


for _ in range(int(input())):
    s = srt(input())
    res = -1
    for p in range(ceil(log2(int(s))), int(log2(int(s[::-1]))) + 1):
        if int(srt(str(pow(2, p)))) == int(s):
            if res == -1:
                res = 0
            res = (res + pow(2, p, MOD)) % MOD
    print(res)
