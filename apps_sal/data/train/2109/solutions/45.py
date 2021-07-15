import math


def slv(A, B):
    A, B = (A, B) if A > B else (B, A)

    # print(, A, B)
    s = A * B
    c = math.floor(math.sqrt(A * B))
    # print(A, B, c)

    if c * (c + 1) < s:
        return 2 * c - 1
    elif A == B:
        return 2 * c - 2
    elif c * c < s:
        return 2 * c - 2
    elif c * (c - 1) < s:
        return 2 * c - 3


# 1
# 12
# 4
# 11
# 14
# 57
# 31
# 671644785


def main():

    Q = int(input())
    for q in range(Q):
        A, B = map(int, input().split())
        print(slv(A, B))


def __starting_point():
    main()
__starting_point()
