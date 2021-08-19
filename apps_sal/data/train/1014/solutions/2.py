from math import log, floor

t = int(input())

while(t > 0):
    n = str(input())
    n1 = int(''.join(sorted(n)))
    n2 = int(''.join(sorted(n, reverse=True)))
    low = pow(2, floor(log(n1, 2)))
    high = pow(2, floor(log(n2, 2)))

    i = low
    ans = 0
    while(i <= high):

        # print(i)
        k = str(i)
        k = ''.join(sorted(k))
        if i >= n1 and int(k) == n1:
            ans += i

        i = i << 1

    mod = 1000000007
    if ans != 0:
        print(ans % mod)
    else:
        print(-1)

    t -= 1
