def is_homogenous(array):
    return len(set(map(type, array))) == 1

def filter_homogenous(arrays):
    return list(filter(is_homogenous, arrays))

