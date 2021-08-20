tc = int(input())
for i in range(0, tc):
    (n, q) = list(map(int, input().split()))
    l = []
    l = list(map(int, input().split()))
    for j in range(0, q):
        (x, y) = list(map(int, input().split()))
        sum = 0
        for k in range(x, y + 1):
            sum = sum + l[k - 1]
        print(sum)
