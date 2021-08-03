def array_center(lst):
    return [i for i in lst if abs(i - sum(lst) * 1.0 / len(lst)) < min(lst)]
