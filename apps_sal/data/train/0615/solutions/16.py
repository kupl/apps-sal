n = int(input())
for i in range(n):
    (a, b) = input().split()
    b = int(b)
    l = list(map(int, input().split()))
    for j in range(b):
        (x, y) = input().split()
        x = int(x) - 1
        y = int(y)
        print(sum(l[x:y]))
