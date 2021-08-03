for _ in range(int(input())):
    # = int(input())
    n, k1, k2 = list(map(int, input().strip().split()))
    p1, p2, p3, p4 = list(map(int, input().strip().split()))
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        j = i
        while j <= n:
            ans[j] += 1
            j += i

    cost = 0
    for i in range(k1, k2 + 1):
        if ans[i] == 3:
            cost += p1
        elif ans[i] % 2 == 1:
            cost += p2
        else:
            cost += p3

    print(cost)
