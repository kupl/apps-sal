def find_slope(points):
    run = points[0] - points[2]
    rise = points[1] - points[3]
    return "undefined" if run == 0 else "%d" % (rise / run)
