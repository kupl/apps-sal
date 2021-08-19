def main():
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    min_y = min(ay, by, cy)
    min_x = min(ax, bx, cx)
    if [ay, by, cy].count(min_y) == 1:
        yy = min_y + 1
    else:
        yy = min_y
    if [ax, bx, cx].count(min_x) == 1:
        xx = min_x + 1
    else:
        xx = min_x
    if xx == yy == 0 and min_x == min_y == 0:
        print((0))
        return
    if xx == yy == 1 and min_x == min_y == 0:
        print((1))
        return
    if min_y < xx:
        x_same = max(abs(xx), abs(min_y)) * 2 - 1
    else:
        x_same = max(abs(xx), abs(min_y)) * 2
    if min_x < yy:
        y_same = max(abs(min_x), abs(yy)) * 2 - 1
    else:
        y_same = max(abs(min_x), abs(yy)) * 2
    #print(x_same, y_same)
    ans = max(x_same, y_same)

    if x_same == y_same:
        ans += 1
    print(ans)


for _ in range(int(input())):
    main()
