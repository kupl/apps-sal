import math
T = int(input())
for i in range(T):
    (N, M, S) = input().split()
    N = int(N)
    M = int(M)
    S = int(S)
    ls = list(map(int, input().split()))
    maxx = max(ls)
    if S < 17 and maxx <= 50:
        ls.sort()
        total_sum = M * S
        count = 0
        sum = 0
        for i in ls:
            if i / S > 2:
                continue
            else:
                sum = sum + math.ceil(i / S) * S
                if sum <= total_sum:
                    count = count + 1
        print(count)
