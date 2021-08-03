def __starting_point():

    n, m, k = list(map(int, input().split()))

    nums = list(map(int, input().split()))

    operations = [tuple(map(int, input().split())) for _ in range(m)]
    op_counter = [0] * (m + 1)
    # queries
    for _ in range(k):
        x, y = list(map(int, input().split()))
        op_counter[x - 1] += 1
        op_counter[y] -= 1

    acc = 0
    offset = [0] * (n + 1)
    for i in range(m):
        l, r, d = operations[i]
        acc += op_counter[i]
        offset[l - 1] += acc * d
        offset[r] -= acc * d

    acc = 0
    for i in range(n):
        acc += offset[i]
        nums[i] += acc
    print(' '.join(map(str, nums)))


__starting_point()
