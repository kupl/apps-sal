import math
t = int(input())
for i in range(t):
    n = int(input())
    avg = []
    arr = list(map(int, input().split()))
    z = max(arr)
    index = arr.index(z)
    s = 0
    j = 1
    for elem in arr:
        s += elem
        avg.append(math.ceil(s / j))
        j += 1
    print(max(avg))
