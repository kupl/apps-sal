for _ in range(int(input())):
    n, increment = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    longVal = arr[-1] + increment
    shortVal = arr[0] - increment
    print(abs(longVal - shortVal))
