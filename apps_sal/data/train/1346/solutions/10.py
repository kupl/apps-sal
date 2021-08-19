from math import ceil
m = int(pow(10, 9) + 7)
t = int(input())
while t:
    t -= 1
    (n, w) = list(map(int, input().split()))
    ss = 0
    for i in range(1, 10):
        for j in range(10):
            if j - i == w:
                ss += 1
    print(ss * pow(10, n - 2, m) % m)
