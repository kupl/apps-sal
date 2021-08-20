a = input().split()
(n, m) = (int(a[0]), int(a[1]))
arr = []
for i in range(n):
    a = input().split()
    a = [int(j) for j in a]
    arr.append(a)
for t in range(int(input())):
    a = input().split()
    (x1, y1, x2, y2) = (int(a[0]), int(a[1]), int(a[2]), int(a[3]))
    total = 0
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            total += arr[i][j]
    print(total)
