def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in [0] * n]
    for i in range(n):
        x, y = xy[i]
        if x > y:
            xy[i] = [y, x]
    xy.sort(key=lambda x: x[0])
    x_list = [x for x, y in xy]
    y_list = [y for x, y in xy]

    max_x = x_list[-1]
    min_x = x_list[0]
    max_y = max(y_list)
    min_y = min(y_list)

    # 左右に分ける解
    ans = (max_x - min_x) * (max_y - min_y)
    if y_list[0] == max_y:
        print(ans)
        return

    width = max_y - min_x
    for i in range(1, n):
        if max_y == y_list[i]:
            break
    min_small = min(y_list[0], x_list[i])
    max_small = max(y_list[0], x_list[n - 1])

    x_list.pop(i)
    y_list.pop(i)

    for i in range(1, n - 1):
        width2 = max_small - min(min_small, x_list[i])
        ans = min(ans, width * width2)
        max_small = max(max_small, y_list[i])
        min_small = min(min_small, y_list[i])
    width2 = max_small - min_small
    ans = min(ans, width * width2)
    print(ans)


main()
