def pattern(n):
    string = ""
    if n < 1:
        return string
    for i in range(1, n + 1):
        string += str(i) * i + "\n"
    return string[0:-1]
