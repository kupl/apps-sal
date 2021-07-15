def problem(a):
    print(a)
    print(type(a))
    try:
        return int(float(a)*50+6)
    except ValueError:
        return "Error"#Easy Points ^_^
