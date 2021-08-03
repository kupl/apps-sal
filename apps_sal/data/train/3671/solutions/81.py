def problem(a):
    if str(a).isdigit():
        num = (int(a) * 50) + 6
        return num
    elif isinstance(a, float):
        num = (a * 50) + 6
        return num
    return "Error"
