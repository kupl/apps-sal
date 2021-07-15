import sys
mod = 10**9 + 7

for _ in range(int(input())):
    x = int(input())
    s = list(map(int, input()))
    ans = len(s)
    for i in range(1, x+1):
        ans = (i + (ans-i) * s[i-1]) % mod
        r = len(s)
        for _ in range(s[i-1]-1):
            if len(s) < x:
                s += s[i:r]
            else:
                break

    print(ans)

