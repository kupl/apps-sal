def main():
    nx, my, k = list(map(int, input().strip().split()))
    my *= 2
    nx *= 2

    diags = [[] for i in range(nx + my)]
    answers = [-1] * k

    for i in range(k):
        x, y = list(map(int, input().strip().split()))

        def add(x, y, i):
            diag_index = nx + (y - x)
            diags[diag_index].append((x, y, i))

        add(x, y, i)
        add(x, my - y, i)
        add(nx - x, y, i)
        add(nx - x, my - y, i)

    cur_t = 0
    cur_x = 0
    cur_y = 0

    while True:
        diag_index = nx + (cur_y - cur_x)
        for x, y, i in diags[diag_index]:
            if answers[i] == -1:
                t = cur_t + (x - cur_x)
                assert(x - cur_x == y - cur_y)
                answers[i] = t

        diff_x = nx - cur_x
        diff_y = my - cur_y
        diff = min(diff_x, diff_y)
        cur_t += diff

        cur_x = (cur_x + diff) % nx
        cur_y = (cur_y + diff) % my

        if (cur_x % (nx // 2)) + (cur_y % (my // 2)) == 0:
            break

    for a in answers:
        print(a)


main()
