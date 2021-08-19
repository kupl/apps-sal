T = int(input())
for i in range(T):
    (N, K) = (int(x) for x in input().split())
    if N > K:
        print(0)
    else:
        print(K // N)
