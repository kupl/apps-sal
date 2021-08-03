from collections import Counter
l = [pow(2, i) for i in range(3321)]

d = {i: Counter(str(i)) for i in l}

t = int(input())
while t:
    x = int(input())
    n = len(str(x))
    dx = Counter(str(x))

    ans = 0
    for i in l:
        if len(str(i)) == n:
            if dx == d[i]:
                ans += i
        elif len(str(i)) > n:
            break

    if ans == 0:
        print(-1)
    else:
        print(ans % 1000000007)

    t -= 1
