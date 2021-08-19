# cook your dish here
T = int(input())
for i in range(0, T):
    N = int(input())
    num = 0
    while (N):
        mod = int(N % 10)
        num = int((num * 10) + mod)
        N = int(N / 10)
    print(num)
