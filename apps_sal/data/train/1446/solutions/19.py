for i in range(int(input())):
    N = int(input())
    binary = (bin(N)[2:])
    if N == 1:
        print(2)
    else:
        if '0' in binary:
            print(-1)
        else:
            print((N - 1) // 2)
