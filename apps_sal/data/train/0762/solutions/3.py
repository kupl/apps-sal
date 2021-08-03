for _ in range(int(input())):
    N = int(input())

    K = 1
    for i in range(N):
        for j in range(N):
            B = bin(K)[2:]
            K += 1
            print(B[::-1], end=" ")
        print()
