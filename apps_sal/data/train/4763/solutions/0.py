def find_variable():
    return next((k for (k, v) in globals().items() if v == 777))
