x = int(input())
for i in range(x):
    (a, b, c) = list(map(int, input().split()))
    for j in range(c // a, -1, -1):
        if a * j + b <= c:
            print(a * j + b)
            break
