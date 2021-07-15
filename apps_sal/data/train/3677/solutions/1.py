def homogenous(a):
    return len(set(map(type, a))) == 1
    
def filter_homogenous(arrays):
    return list(filter(homogenous, arrays))
