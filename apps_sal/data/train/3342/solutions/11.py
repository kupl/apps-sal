def pattern(n):
    if n < 1:
        return ""
    else:
        string = ""
        for i in range(1, n):
            string += str(i) * i + "\n"
        string += str(n) * n
        return string
