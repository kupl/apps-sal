t = int(input())
for i in range(t):
    n = int(input())
    coordinates_x = {}
    coordinates_y = {}
    for j in range(4 * n - 1):
        coord = input().split()
        x_axis = coordinates_x.get(int(coord[0]), [])
        x_axis.append(int(coord[1]))
        coordinates_x[int(coord[0])] = x_axis
        y_axis = coordinates_y.get(int(coord[1]), [])
        y_axis.append(int(coord[0]))
        coordinates_y[int(coord[1])] = y_axis
    for (k, v) in coordinates_x.items():
        if len(v) % 2 != 0:
            x_coord = k
    for (k, v) in coordinates_y.items():
        if len(v) % 2 != 0:
            y_coord = k
    print(x_coord, y_coord)
