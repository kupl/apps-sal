def closest(lst):
    min_v = min(lst, key=lambda x: abs(x))
    return None if -min_v in lst and min_v else min_v
