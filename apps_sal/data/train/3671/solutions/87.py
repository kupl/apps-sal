def problem(a):
    value = a
    if (isinstance(value, str)):
        return "Error"
    else:
        value = value * 50 +6
        return value
