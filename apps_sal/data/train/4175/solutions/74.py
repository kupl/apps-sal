def repeater(string, n):
    if n == 1:
        return string
    else:
        return repeater(string, n - 1) + string
