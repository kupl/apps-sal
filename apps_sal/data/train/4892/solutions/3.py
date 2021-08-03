def find_biggTriang(ps):
    n = len(ps)
    count = 0
    max_area = -1.0
    max_area_triangles = []
    for i in xrange(n):
        for j in xrange(i + 1, n):
            dx1, dy1 = ps[j][0] - ps[i][0], ps[j][1] - ps[i][1]
            for k in xrange(j + 1, n):
                dx2, dy2 = ps[k][0] - ps[i][0], ps[k][1] - ps[i][1]
                a = abs(0.5 * (dx1 * dy2 - dx2 * dy1))
                count += a != 0
                if a < max_area:
                    continue
                triangle = [ps[i], ps[j], ps[k]]
                if a > max_area:
                    max_area = a
                    max_area_triangles = [triangle]
                elif a == max_area:
                    max_area_triangles.append(triangle)
    max_area_triangles = [map(list, tr) for tr in max_area_triangles]
    if len(max_area_triangles) == 1:
        max_area_triangles = max_area_triangles[0]
    return [n, n * (n - 1) * (n - 2) // 6, count, max_area_triangles, max_area]
