for _ in range(int(input())):
    (a, b) = map(int, input().split())
    ans = 1
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            if i > ans:
                ans = i
    print(ans)
