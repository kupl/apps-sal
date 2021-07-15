def move_zeros(array):
    a = list(filter(lambda x: x!=0 or type(x) is bool, array))
    return a + [0]*(len(array)-len(a))
