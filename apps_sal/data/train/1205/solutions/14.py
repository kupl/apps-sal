t = int(input())
for _ in range(t):
    s = input()
    k = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            k += 1
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            ans += k
            if i == 0:
                pass
            elif s[i - 1] == s[i]:
                ans -= 1
            else:
                ans += 1
            if j == len(s) - 1:
                pass
            elif s[j + 1] == s[j]:
                ans -= 1
            else:
                ans += 1
    print(ans)
