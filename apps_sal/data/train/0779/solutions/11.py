t = int(input())
for i in range(t):
    n = input()
    arr = [int(i) for i in input().split()]
    arr.sort()
    while(len(arr) != 1):
        w = arr[-1]
        arr.pop()
        e = arr[-1]
        arr.pop()
        arr.append((w + e) / 2)
    print('%.6f' % arr[0])
