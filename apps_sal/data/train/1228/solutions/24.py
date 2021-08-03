t = int(input())
for _ in range(t):
    n = int(input())
    x_points = {}
    y_points = {}
    for i in range(4 * n - 1):
        x, y = map(int, input().split())
        x_points[x] = x_points.setdefault(x, 0) + 1
        y_points[y] = y_points.setdefault(y, 0) + 1

    for x in x_points:
        if x_points[x] % 2 == 1:
            print(x, end=" ")

    for y in y_points:
        if y_points[y] % 2 == 1:
            print(y, end=" ")
