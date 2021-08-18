
def bsearch(target, min_i, max_i, func):
    if func(max_i) < target:
        return max_i
    if target <= func(min_i):
        return None
    index = (max_i + min_i) // 2
    while True:
        if max_i - min_i <= 1:
            return min_i
        if func(index) < target:
            index, min_i = (index + max_i) // 2, index
            continue
        index, max_i = (index + min_i) // 2, index


def f(N):
    def g(i):
        if i < I or J < i:
            return i * (N - i + 1)
        elif i == I:
            return 0
        elif I < J:
            return i * (N - i + 2)
        else:
            return i * (N - i)
    I, J = A, N - B + 1
    return max(g(N // 2), g(N // 2 + 1), g(N // 2 + 2))


Q, = list(map(int, input().split()))
for _ in range(Q):
    A, B = list(map(int, input().split()))
    r = bsearch(A * B, 1, A * B, f)
    print((r - 1))
