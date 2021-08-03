def main():
    import sys
    from operator import itemgetter
    input = sys.stdin.readline

    N = int(input())
    if N == 1:
        print((0))
        return
    xy = []
    ymax = 0
    ymin = 10**9 + 7
    for _ in range(N):
        x, y = list(map(int, input().split()))
        if x > y:
            x, y = y, x
        if y > ymax:
            ymax = y
        if y < ymin:
            ymin = y
        xy.append((x, y))
    xy.sort(key=itemgetter(0))

    xmin = xy[0][0]
    xmax = xy[-1][0]
    ymax_idx = []
    for i in range(N):
        if xy[i][1] == ymax:
            ymax_idx.append(i)

    ans = (xmax - xmin) * (ymax - ymin)
    xmin_tmp = 10**9 + 7
    xmax_tmp = 0
    for i in range(ymax_idx[0]):
        if xy[i][1] < xmin_tmp:
            xmin_tmp = xy[i][1]
        if xy[i][1] > xmax_tmp:
            xmax_tmp = xy[i][1]
        ans_new = (ymax - xmin) * (max(xmax, xmax_tmp) - min(xmin_tmp, xy[i + 1][0]))
        if ans_new < ans:
            ans = ans_new
    xmin_tmp = 10 ** 9 + 7
    xmax_tmp = 0
    for i in range(N - 1, ymax_idx[-1], -1):
        if xy[i][1] < xmin_tmp:
            xmin_tmp = xy[i][1]
        if xy[i][1] > xmax_tmp:
            xmax_tmp = xy[i][1]
        ans_new = (ymax - xmin) * (max(xmax_tmp, xy[i - 1][0]) - min(xmin_tmp, xmin))
        if ans_new < ans:
            ans = ans_new

    print(ans)


def __starting_point():
    main()


__starting_point()
