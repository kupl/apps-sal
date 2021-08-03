t = int(input())
for _ in range(t):
    N = int(input())
    K = int(input())
    num_1 = K % N
    num_0 = N - num_1
    ans = 0
    if num_1 > num_0:
        ans = num_0 * 2
    elif num_0 > num_1:
        ans = num_1 * 2
    else:
        ans = num_1 * 2 - 1
    print(ans)
