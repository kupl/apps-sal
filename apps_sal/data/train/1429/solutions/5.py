k = 30
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(float, input().split()))
    ans = 0
    for i in range(k):
        p = 0
        for j in range(n):
            if(l1[j] & (1 << i)):
                p = p * (1 - l2[j]) + (1 - p) * l2[j]
        ans += p * (1 << i)

    print("%.15f" % ans)
