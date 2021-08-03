from math import sqrt as S
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('INFINITY')
        continue
    else:
        ans = 0
        z = int(S(n))
        for i in range(2, z + 1):
            temp = n
            while temp:
                r = temp % i
                temp = temp // i
            if r == 1:
                ans += 1
        k = n // 2
        if n > k:
            ans += n - k
        print(ans)
