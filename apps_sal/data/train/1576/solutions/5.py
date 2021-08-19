t = int(input())
for i in range(t):
    k = int(input())
    arr = []
    for i in range(1, k + 1):
        arr.append(i)
    for i in range(k):
        for j in range(i, k):
            print(arr[j], end='')
        for j in range(0, i):
            print(arr[j], end='')
        print()
