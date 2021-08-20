def find_variable():
    return next((k for k in globals() if eval(k) == 777))
