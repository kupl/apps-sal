def find_slope(points):
    x1, y1, x2, y2 = points
    return "undefined" if x2 - x1 == 0 else str((y2 - y1) // (x2 - x1))


# def find_slope(points):
#     try:
#         return str((points[3] - points[1]) / (points[2] - points[0]))
#     except ZeroDivisionError:
#         return "undefined"

# def find_slope(points):
#     a,b,c,d = points
#     return 'undefined' if a == c else str((b - d) / (a - c))
