def bar_triang(*points):
    center_x = sum((point[0] for point in points)) / len(points)
    center_y = sum((point[1] for point in points)) / len(points)
    return [round(center_x, 4), round(center_y, 4)]
