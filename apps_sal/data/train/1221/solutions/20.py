import math


def binarySearch(arr, l, r, x):
    mid = (l + r) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch(arr, l, mid - 1, x)
    elif (arr[mid] < x and arr[mid + 1] > x):
        return mid
    else:
        return binarySearch(arr, mid + 1, r, x)


def vceil(k):
    if(math.ceil(k) == k):
        return int(k + 1)
    else:
        return math.ceil(k)


dp = [1]
i = 1
sum = 0
while(i <= 10**9):
    sum += i**2
    i = math.sqrt(sum)
    i = vceil(i)
    dp.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    ans = binarySearch(dp, 0, len(dp), n)
    ans = ans + 1
    print(ans)
