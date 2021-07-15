def is_triangle(a, b, c):
    lst = [int(a),int(b),int(c)]
    lst = sorted(lst)
    if lst[0]+lst[1]>lst[2]:
        return True
    else:
        return False

