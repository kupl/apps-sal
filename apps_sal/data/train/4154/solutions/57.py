def is_triangle(a, b, c):
    lst = sorted([a, b, c])
    if lst[2] - lst[1] < lst[0] and lst[0] + lst[1] > lst[2]:
        return True
    else:
        return False
