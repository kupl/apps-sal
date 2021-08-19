import math as m
for _ in range(int(input())):
    length = int(input())
    arr = list(map(int, input().split()))
    if length == 2:
        print(arr[0] + arr[1])
    else:
        tmparr = list(set(arr))
        tmparr.sort()
        fmax = tmparr.pop()
        smax = tmparr.pop()
        p = len(tmparr)
        if p == 0:
            print(fmax + smax)
        else:
            result = tmparr[0]
            for i in range(1, p):
                result = m.gcd(tmparr[i], result)
            gcd0 = result
            gcdH = m.gcd(gcd0, fmax)
            gcdSH = m.gcd(gcd0, smax)
            case11 = fmax + gcdSH
            case22 = smax + gcdH
            print(max(case11, case22))
