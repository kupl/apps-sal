def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    xor_all = A[0]
    
    for i in range(1, N):
        xor_all ^= A[i]

    for i in range(N):
        if i != N - 1:
            print(A[i]^xor_all, end=" ")
        else:
            print(A[i]^xor_all)

def __starting_point():
    main()
__starting_point()
