def find_variable():
    return [k for (k, v) in globals().items() if v == 777][0]
