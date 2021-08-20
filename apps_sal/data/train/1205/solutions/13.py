t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    k = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            k += 1
    ans = k * (n * (n + 1) // 2)
    for i in range(n):
        x = n - i
        if i == 0:
            pass
        elif s[i] == s[i - 1]:
            ans -= x
        else:
            ans += x
        x = i + 1
        if i == n - 1:
            pass
        elif s[i + 1] == s[i]:
            ans -= x
        else:
            ans += x
    print(ans)
