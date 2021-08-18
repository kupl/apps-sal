def find_outlier(integers):
    determinant = [x for x in integers[:3] if x % 2 == 0]
    if len(determinant) > 1:
        mod = 1
    else:
        mod = 0
    for i in integers:
        if i % 2 == mod:
            return i
