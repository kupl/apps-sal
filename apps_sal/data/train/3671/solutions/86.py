def problem(a):
    value = 0
    if isinstance(a, str):
        return "Error"
    else: 
        value = (a * 50)
        value = value + 6
        return value
