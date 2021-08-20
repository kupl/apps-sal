t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    a = a[::-1]
    arr = [1]
    for i in range(1, n):
        if a[i - 1] < 0 and a[i] >= 0 or (a[i - 1] >= 0 and a[i] < 0):
            arr.append(1 + arr[i - 1])
        else:
            arr.append(1)
    print(' '.join((str(i) for i in arr[::-1])))
