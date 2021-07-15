def pattern(n):
    if(n < 1):
        return ""
    else:
        s = ""
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                s += str(i)
            if(i != n):
                s += "\n"
        return s
