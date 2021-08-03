t = int(input())

for _ in range(t):
    n = int(input())

    a = [int(x) for x in input().split()]
    f = []

    for i in range(n):
        for j in range(i + 1, n):
            f.append(a[i] + a[j])

    maxi = f.count(max(f))
    ans = maxi / len(f)

    print(format(ans, '.6f'))
