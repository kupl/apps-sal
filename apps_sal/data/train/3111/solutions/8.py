def number_format(n):
    n = [x for x in str(n)]
    if n[0] == "-":
        n = n[1:]
        result = "-"
    else:
        result = ""
    end = []
    while len(n) > 3:
        end.append("".join([","] + n[-3:]))
        n = n[:-3]
    end.append("".join(n))
    for x in end:
        result += end[-1]
        end = end[:-1]
    return result
