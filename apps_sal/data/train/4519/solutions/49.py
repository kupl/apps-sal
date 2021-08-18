def max_number(n):
    return int("".join([str(i) for i in sorted([int(x) for x in str(n)], reverse=True)]))
