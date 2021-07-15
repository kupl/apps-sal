def cat_mouse(x):
    n = x.count(".")
    if n <= 3:
        return ("Caught!")
    if n > 3:
        return ("Escaped!")
