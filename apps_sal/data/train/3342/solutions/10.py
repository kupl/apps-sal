def pattern(n):
    pat = ""
    for i in range(1, n):
        pat += str(i) * i + "\n"
    pat += str(n) * n
    return pat
