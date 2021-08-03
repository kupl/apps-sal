t = int(input())
while t > 0:
    t -= 1
    arr = list(map(int, input().split()))
    k = int(input())
    arr.sort()
    b = arr[0]
    g = arr[1]
    r = arr[2]
    if k <= b:
        print((k - 1) * 3 + 1)
    elif k <= g:
        print(3 * b + (k - b - 1) * 2 + 1)
    elif k <= r:
        print(2 * g + b + k - g)
