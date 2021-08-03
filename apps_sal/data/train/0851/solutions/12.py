# cook your dish here
T = int(input())
for i in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    a = 2 * (N - (N - 1) / K)
    print(a)
