for _ in range(int(input())):
    n = int(input())
    s = input()
    q = 0
    ans = 0
    for i in s:
        if i == '(':
            q += 1
        else:
            if q > 0:
                q -= 1
            else:
                ans += 1
    print(ans)
