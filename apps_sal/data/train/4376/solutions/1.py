def count_pal(n):

    def x(y):
        return 9 * int(10 ** ((y - 1) // 2))
    return [x(n), sum((x(i) for i in range(n + 1)))]
