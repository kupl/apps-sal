t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    list1 = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            list1.append(a[i] + a[j])
    c = 0
    c = max(list1)
    d = 0
    d = n * (n - 1) // 2
    c1 = 0
    c1 = list1.count(c)
    print(c1 / d)
