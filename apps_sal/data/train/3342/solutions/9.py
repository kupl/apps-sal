def pattern(n):
    if n > 0:
        m = "1"
        for i in range(1, n):
            h = ""
            for j in range(i + 1):
                h += str(i + 1)
            m += "\n" + h
        return m
    else:
        return ""
