3

def main():
    N = int(input())
    A = []
    for i, _ in enumerate(range(N)):
        a, b, c, d = [int(e) for e in input().split(' ')]
        A.append((-(a + b + c + d), i + 1))

    A.sort()

    for i in range(N):
        if A[i][1] == 1:
            print(i + 1)


def __starting_point():
    main()

__starting_point()
