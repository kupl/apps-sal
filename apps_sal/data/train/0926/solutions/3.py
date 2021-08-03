# cook your dish here
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    x = [int(i)for i in input().split()]
    a = []
    count = 0
    for i in x:
        a.append(i)
        t = a[:]
        t.sort()
        if len(t) >= 2:
            if t[-1] + t[-2] <= k and len(t) > count:
                count = len(t)
            else:
                a.pop(0)
    print(count)
