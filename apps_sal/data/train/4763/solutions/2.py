def find_variable():
    for k, v in globals().items():  # k = name of variable, v = value of variable
        if v == 777:
            return k
