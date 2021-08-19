3


def solve(N, A):
    A.sort()
    i = 0
    j = 0
    c = 0
    while j < N:
        while j < N and A[j] == A[i]:
            j += 1
        if j == N:
            break
        c += 1
        i += 1
        j += 1
    return c


def main():
    N = int(input())
    A = [int(e) for e in input().split(' ')]
    print(solve(N, A))


def __starting_point():
    main()


__starting_point()
