t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    max = 0
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] + l[j] > max:
                max = l[i] + l[j]
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] + l[j] == max:
                c += 1
    x = n * (n - 1) / 2
    print(c / x)
    t -= 1
