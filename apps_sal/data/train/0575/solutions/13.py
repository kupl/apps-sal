t = int(input())
for _ in range(t):
    s = input().replace('=', '')
    if len(s) == 0:
        print(1)
        continue
    (ans, count) = (0, 1)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            ans = max(ans, count)
            count = 1
    ans = max(count, ans)
    print(ans + 1)
