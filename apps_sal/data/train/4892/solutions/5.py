def area_triangel(i):
    return abs(1/2*(i[0][0]*i[1][1]+i[0][1]*i[2][0]+i[1][0]*i[2][1]-i[2][0]*i[1][1]-i[2][1]*i[0][0]-i[1][0]*i[0][1]))

def find_biggTriang(listPoints):
    import itertools
    max_points = []
    max_area = -1000
    every_valid_point = list(itertools.combinations(listPoints, 3))
    num_invalid_points = 0
    for j in every_valid_point:
        area = area_triangel(j)
        if area == 0:
            num_invalid_points += 1
        elif area > max_area:
            max_area, max_points = area, []
            max_points.append(list(list(x) for x in j))
        elif area == max_area:
            max_points.append(list(list(x) for x in j))

    return [len(listPoints), len(every_valid_point), len(every_valid_point)-num_invalid_points, max_points[0] if len(max_points) == 1 else max_points ,max_area]
