for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 'YES'
    if n <= 6:
        x = l.count(1)
        if x > 1:
            ans = 'NO'
    else:
        for i in range(n - 5):
            x = l[i:i + 6].count(1)
            if x > 1:
                ans = 'NO'
                break
    print(ans)
