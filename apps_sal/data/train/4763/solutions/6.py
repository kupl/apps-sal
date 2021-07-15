def find_variable():
    for i in globals():
        if eval(i) == 777:
            return i
