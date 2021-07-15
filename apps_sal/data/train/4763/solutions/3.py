find_variable = lambda: next(var for var, val in globals().items() if val == 777)
