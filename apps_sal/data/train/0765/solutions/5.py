import math


def solve(array, r):
    i, res, tmp1, tmp2 = 0, 1, 1, 1
    while i * r < len(array):
        res *= array[i * r]
        res %= 10**9 + 7
        tmp1 = float(array[i * r]) / 10 ** int(math.log(array[i * r], 10))
        tmp2 *= tmp1
        tmp2 = float(tmp2) / 10 ** int(math.log(tmp2, 10))
        i += 1
    first_digit = int(tmp2 // 10 ** int(math.log(tmp2, 10)))
    return ' '.join((str(first_digit), str(res)))


def frjump():
    N = int(input())
    friendliness = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            friendliness[query[1] - 1] = query[2]
        else:
            types, R = query
            print(solve(friendliness, R))


def __starting_point():
    frjump()


__starting_point()
