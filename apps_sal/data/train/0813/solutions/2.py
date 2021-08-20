def func(n):
    sum = 0
    if k == 1:
        for i in l:
            sum += abs(n - i)
        return sum
    if k == 2:
        for i in l:
            sum += (n - i) ** 2
        return sum
    if k == 3:
        for i in l:
            sum += abs(n - i) ** 3
        return sum


def findPeakUtil(low, high, n):
    mid = low + (high - low) // 2
    one = func(mid - 1)
    two = func(mid)
    three = func(mid + 1)
    if (mid == 0 or one >= two) and (mid == n - 1 or three >= two):
        return mid
    elif mid > 0 and one < two:
        return findPeakUtil(low, mid - 1, n)
    else:
        return findPeakUtil(mid + 1, high, n)


def findPeak(n):
    return findPeakUtil(0, n - 1, n)


(n, k) = map(int, input().split())
l = list(map(int, input().split()))
print(findPeak(max(l) + 2))
