def get_result(r, c, dims):
    if len(dims) == 0:
        if r * c == 0:
            return 1
        return 0
    for i in range(len(dims)):
        newdims = [dims[x] for x in range(len(dims)) if x != i]
        if r != 0 and dims[i] % r == 0:
            if get_result(r, c - dims[i] / r, newdims):
                return 1
        if c != 0 and dims[i] % c == 0:
            if get_result(r - dims[i] / c, c, newdims):
                return 1
    return 0


def __starting_point():
    num = int(input())
    for i in range(num):
        (R, C, M, K, J) = [int(x) for x in input().split()]
        if get_result(R, C, [M, K, J]):
            print('Yes')
        else:
            print('No')


__starting_point()
