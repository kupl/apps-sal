#!python3

# input
Q = int(input())
A, B = [None] * Q, [None] * Q
for i in range(Q):
    A[i], B[i] = sorted(map(int, input().split()))


def solve(a, b):
    w = a * b - 1
    left, right = 0, b - a
    while right - left > 1:
        x = (left + right) // 2
        v = w // (a + x)
        if v < a:
            right = x
        else:
            left = x

    n = left
    left, right = 0, n
    while right - left > 1:
        x = (left + right) // 2
        v = w // (a + x)
        if v < a + x:
            right = x
        else:
            left = x

    return right + (w // (a + right)) - (w // (a + n))


def main():
    for a, b in zip(A, B):
        ans = 2 * (a - 1) + solve(a, b)
        print(ans)


def __starting_point():
    main()

__starting_point()
