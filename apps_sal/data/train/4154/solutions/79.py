def is_triangle(a, b, c):
    list_ = [a, b, c]
    return True if sorted(list_)[0] + sorted(list_)[1] > sorted(list_)[2] and sorted(list_)[0] > 0 and sorted(list_)[1] > 0 and sorted(list_)[2] > 0 else False
