T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    prefix = []
    prefix.append(A[0])
    for i in range(1, N):
        prefix.append(prefix[i - 1] + A[i])

    reach = 0
    days = 0
    while(reach < N - 1):
        reach = reach + prefix[reach]
        days += 1
    print(days)
