t = int(input())
while t > 0:
    t = t - 1
    n = int(input())
    k = int(input())
    num_1 = k % n
    num_0 = n - num_1
    ans = 0
    if num_0 > num_1:
        ans = num_1 * 2
    elif num_0 < num_1:
        ans = num_0 * 2
    else:
        ans = num_1 * 2 - 1
    print(ans)
