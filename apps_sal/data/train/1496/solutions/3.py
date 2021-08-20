t = int(input())
for i in range(t):
    s = input().strip()
    level = 1
    ans = 1
    for i in s:
        if level % 2 == 0:
            if i == 'l':
                ans = 2 * ans - 1
            else:
                ans = 2 * ans + 1
        elif i == 'l':
            ans = 2 * ans
        else:
            ans = 2 * ans + 2
        ans = ans % 1000000007
        level += 1
    print(ans)
