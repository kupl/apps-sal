def problem(a):
    try:
        return float(a) * 50 + 6
    except ValueError:
        return "Error"
