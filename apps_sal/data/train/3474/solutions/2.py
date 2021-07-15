def pattern(n):
    return "\n".join("{}{}{}".format(1 if i else "", "*" * i, i+1) for i in range(n))

