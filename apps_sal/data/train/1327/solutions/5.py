t = int(input())
for i in range(t):
    n, q = list(map(int, input().split()))
    cities = list(map(int, input().split()))
    for j in range(int(q)):
        q1, q2 = list(map(int, input().split()))
        a = cities[q1 - 1]
        b = cities[q2 - 1]
        if (a > b):
            c = a
            a = b
            b = c
        size = 0
        for c in cities:
            if c >= a and c <= b:
                size += 1
        print(q2 - q1 + b - a, size)
