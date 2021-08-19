# python3
n, k = [int(x) for x in input().split()]

begin = 1
if k == 1:
    for x in range(1, n + 1):
        print(x, end=" ")
else:
    # k = 2, +2 -1: 1 3 2
    # k = 3, +3 -2 + 1: 1 4 2 3
    # k = 4, +4 -3 + 2 -1: 1 5 2 4 3
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

    # for z in range((k+1)/2):
    # 	# Difference continues to decrease by 1
    # 	print(diff + z, end=" ")
    # 	print(n - z, end=" ")
    # if k % 2 == 0:
    # 	print((diff+n)//2)
