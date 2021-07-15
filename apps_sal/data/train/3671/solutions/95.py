def problem(a):
    try:
        v = float(a)
        return 50 * v + 6
    except Exception as e:
        return "Error"
