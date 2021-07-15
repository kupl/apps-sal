def triangular_range(start, stop):
    dict = {}
    for trial in range(1, stop + 1):
        triangle_num = sum(range(trial + 1))
        if  start <= triangle_num <= stop:
            dict[trial] = triangle_num
    return dict


