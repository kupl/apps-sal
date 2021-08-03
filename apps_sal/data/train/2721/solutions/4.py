def pyramid(n):
    s = ""
    for i in range(n - 1):
        s += (" " * ((n - i - 1)) + "/" + " " * (i * 2) + "\\\n")
    s += ("/" + "_" * ((n * 2) - 2) + "\\\n")
    return s
