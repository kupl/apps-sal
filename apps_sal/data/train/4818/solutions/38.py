def solution(a, b):
    arr_sorted = sorted([a, b], key=len)
    return "".join([arr_sorted[0], arr_sorted[1], arr_sorted[0]])
