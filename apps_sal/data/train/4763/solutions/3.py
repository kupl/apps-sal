def find_variable():
    return next((var for (var, val) in globals().items() if val == 777))
