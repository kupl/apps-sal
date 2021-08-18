def isValid(arr, mid):
    t = 0.0
    for i in range(len(arr)):
        if t < arr[i]:
            t = arr[i] + mid
        elif t <= arr[i] + d:
            t = t + mid
        else:
            return False
    return True


for _ in range(int(input())):
    n, d = list(map(int, input().split(' ')))
    arr = [int(num) for num in input().split(' ')]
    duration = []
    ans = -1
    arr.sort()

    left = 0.0
    right = 10000000000
    while right - left >= 10**(-6):
        mid = (left + right) / 2
        if isValid(arr, mid) == True:
            left = mid
            ans = mid
        else:
            right = mid

    print(ans)
