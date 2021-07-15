def is_triangle(a, b, c):
    list_ = [a, b, c]
    if sorted(list_)[0] + sorted(list_)[1] > sorted(list_)[2]:
        if sorted(list_)[0] > 0 and sorted(list_)[1] > 0 and sorted(list_)[2] > 0:
            return True
    return False
