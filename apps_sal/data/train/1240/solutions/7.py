for _ in range(int(input())):
    n = input()
    ar = list(map(int, input().split()))
    ans = 0
    for i in ar:
        if i % 6 == 0:
            ans += 6
        else:
            ans += i % 6
    print(ans)
