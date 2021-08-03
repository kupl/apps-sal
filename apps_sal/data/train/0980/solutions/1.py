# cook your code here
t = int(input())
while (t > 0):
    t = t - 1
    T = 0
    N, B, M = list(map(int, input().split()))
    while(N != 0):
        T = T + int((N + 1) / 2) * M + B
        M = 2 * M
        N = int(N / 2)
    print(T - B)
