for _ in range(int(input())):
    s = input()
    se = set()
    ans = 0
    for i in s:
        se.add(i)
        ans += 1
        if len(se) == 10:
            break
    print(ans)
