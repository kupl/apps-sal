from functools import reduce
T = int(input())
for i in range(T):
    count = 0
    a = 0
    b = 0
    Count = 0
    N, K = map(int, input().split())
    S = str(input().lower())
    for j in S:
        if j == 'a':
            a += 1
        elif j == 'b':
            b += 1
            count += a
    Count = (K * (K - 1) * a * b) // 2
    Count = Count + K * count
    print(Count)
