def check_exam(arr1, arr2):
    point = 0
    for x, y in zip(arr1, arr2):
        if x != y:
            if y != "":
                point -= 1
            else:
                point = point + 0
        elif x == y:
            point += 4
    if point < 0:
        return 0
    else:
        return point
