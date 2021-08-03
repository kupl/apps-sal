from math import ceil
for i in range(eval(input())):
    n = eval(input())
    arr = list(map(int, input().split()))
    while max(arr) != min(arr):
        arr.sort()
        mini = float(arr[0])
        for i in range(n):
            fac = int(ceil(arr[i] / mini)) - 1
            arr[i] -= mini * fac
    print(int(sum(arr)))
