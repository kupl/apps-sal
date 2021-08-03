tests = int(input())
for test in range(tests):
    n = int(input())
    a = [int(i) for i in input().split()]
    x = -1
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            x = i
            break
    if x == -1:
        print(0)
        continue
    y = -1
    for i in range(x - 1, -1, -1):
        if a[i] > a[i + 1]:
            y = i
            break
    if y == -1:
        print(0)
        continue
    print(y + 1)
