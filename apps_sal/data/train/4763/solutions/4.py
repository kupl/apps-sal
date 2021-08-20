def find_variable():
    for (k, v) in globals().items():
        if v == 777:
            return k
