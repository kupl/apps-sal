def problem(a):
    try:
        if type(a) != str:
            a = float(a) * 50 + 6
        else:
            a = "Error"
    except ValueError:
        a = float(a) * 50 + 6
    except TypeError:
        a = "Error"
    return a
