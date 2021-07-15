def problem(a):
    z = lambda a: "Error" if str(a).isalpha() else a*50 + 6
    return z(a)
