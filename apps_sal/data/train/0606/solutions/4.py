from math import log
try:
    for i in range(int(input())):
        a = input().split(' ')
        (n, k, x, m) = map(int, a)
        ans = 'no'
        u = 0
        if k != 2 and k != 1:
            if x % k == 0:
                x //= k
                u = -1
            elif x % k == 1:
                n -= 1
                x //= k
                u = -1
            if u == -1:
                while x != 0:
                    if x % k == 0:
                        x //= k
                    elif x % k == 1:
                        x //= k
                        n -= 1
                    elif x % k == 2:
                        x //= k
                        n -= 2
                    else:
                        break
            if n == 0 and x == 0:
                ans = 'yes'
        elif k == 1:
            if x == n:
                ans = 'yes'
        else:
            lst = []
            p = 0
            N = n
            while x != 0:
                if x % 2 == 0:
                    x //= 2
                    p += 1
                elif x % 2 == 1:
                    x //= 2
                    n -= 1
                    p += 1
                    lst.append(2 ** (p - 1))
            if len(lst) == N:
                ans = 'yes'
            if len(lst) < N:
                k = 0
                g = len(lst)
                if lst[0] > 2:
                    g += int(log(lst[0]) // log(2)) - 1
                    k = 1
                for i in range(1, len(lst)):
                    if k == 1:
                        g += int(log(lst[i] // lst[i - 1], 2))
                    elif lst[i] > 2 * lst[i - 1]:
                        g += int(log(lst[i] // lst[i - 1], 2)) - 1
                        k = 1
                    else:
                        k = 0
                if g >= N:
                    ans = 'yes'
        print(ans)
except EOFError as e:
    pass
