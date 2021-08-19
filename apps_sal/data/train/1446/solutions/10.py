# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    f = bin(N)[2:]
    if f.count('0') == 0:
        if N == 1:
            print(2)
        else:
            print(N >> 1)
    else:
        print(-1)
