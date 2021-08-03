t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = []
    arr3 = []
    for i in range(n):
        x, y = map(int, input().strip().split(" "))
        arr.append(y - x)
        arr3.append(y + x)
    arr = sorted(arr)
    arr3 = sorted(arr3)
    arr2 = []
    for i in range(n - 1):
        arr2.append((arr[i + 1] - arr[i]) / 2)
        arr2.append((arr3[i + 1] - arr3[i]) / 2)
    print(min(arr2))
