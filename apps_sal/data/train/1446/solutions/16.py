T = int(input())
for i in range(T):
    N = int(input())
    b = bin(N)[2:]

    if N == 1:
        print(2)
    else:
        if '0' in b:
            print(-1)
        else:
            print((N - 1) // 2)
