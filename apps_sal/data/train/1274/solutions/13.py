t = int(input())
for i in range(t):
    k = int(input())
    l = []
    for i in range(1, 101):
        l.append(i)
    arr = []
    x = 1
    for i in range(2 * 100):
        if i % 2 == 0:
            arr.append([x] * 100)
            x = x + 1
        else:
            arr.append(l)
    j = 0
    while j < k:
        i = 0
        while i < 2 * k:
            print(arr[i][j], end='')
            i = i + 1
        print()
        j = j + 1
