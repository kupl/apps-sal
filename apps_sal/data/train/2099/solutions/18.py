n, k = [int(x) for x in input().split()]

begin = 1
if k == 1:
    for x in range(1, n + 1):
        print(x, end=" ")
else:
    for y in range(n - k - 1):
        print(begin + y, end=" ")
    diff = n - k
    high = n
    while high >= diff + 1:
        print(diff, end=" ")
        print(high, end=" ")
        diff += 1
        if diff == high:
            break
        high -= 1
    if diff == high and k % 2 != 1:
        print(high)
