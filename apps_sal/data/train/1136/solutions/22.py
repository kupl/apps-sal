T = int(input())
for i in range(T):
    N, K = [int(i) for i in input().split()]
    if N % 2 == 0:
        print((N // 2) * K)
    else:
        print(((N // 2 + 1) * K))  # cook your dish here
