m = int(pow(10, 9) + 7)
for i in range(int(input())):
    (n, w) = list(map(int, input().split()))
    s = 0
    for i in range(1, 10):
        for j in range(10):
            if j - i == w:
                s += 1
    print(s * pow(10, n - 2, m) % m)
