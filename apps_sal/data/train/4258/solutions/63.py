def series_sum(n):
    output = 0
    for i in range(n):
        output += 1 / (1 + (i * 3))
    if len(str(round(output, 2))) < 4:
        if str(round(output, 2)) != "0":
            a = str(round(output, 2))
            a += "0"
            return a
        else:
            return "0.00"
    else:
        return str(round(output, 2))
