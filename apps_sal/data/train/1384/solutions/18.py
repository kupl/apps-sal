# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(input())
    l1 = [0] * n
    l2 = [0] * n
    for i in range(1, n):
        if l[i - 1] == "1":
            l1[i] = l1[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if l[i + 1] == "1":
            l2[i] = l2[i + 1] + 1
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (l1[i] + l2[i + k - 1] + k))
    # print(l1)
    # print(l2)
    print(ans)
