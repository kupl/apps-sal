for u in range(int(input())):
    n = int(input())
    x = [int(w) for w in input().split()]
    ans = 0
    for i in range(1, n):
        c = 0
        for j in range(i):
            if x[j] % x[i] == 0:
                c += 1
        ans = max(ans, c)
    print(ans)
