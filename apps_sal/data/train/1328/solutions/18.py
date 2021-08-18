for _ in range(int(input())):
    s = input().strip()
    ans = 0
    for i in s:
        if i != '4' and i != '7':
            ans += 1
    print(ans)
