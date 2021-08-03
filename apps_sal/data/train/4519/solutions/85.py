def max_number(n):
    return int("".join(list(map(str, sorted(list([int(x) for x in list(str(n))]), reverse=True)))))
