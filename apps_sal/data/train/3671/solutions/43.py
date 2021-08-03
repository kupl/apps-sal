def problem(a):
    if type(a) == int or type(a) == float:
        print(a)
        return a * 50 + 6
    else:
        print(a)
        return "Error"
