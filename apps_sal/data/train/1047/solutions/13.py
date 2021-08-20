for k in range(int(input())):
    n = int(input())
    arr1 = []
    arr2 = []
    for _ in range(n):
        (a, b) = map(int, input().split())
        arr1.append(a + b)
        arr2.append(b - a)
    arr1.sort()
    arr2.sort()
    l1 = []
    l2 = []
    for i in range(len(arr1) - 1):
        l1.append(arr1[i + 1] - arr1[i])
        l2.append(arr2[i + 1] - arr2[i])
    x = min(l1)
    y = min(l2)
    print('{0:.6f}'.format(min(x, y) / 2))
