def max_number(n):
    # your code her
    return int("".join([str(i) for i in sorted([int(x) for x in str(n)], reverse=True)]))
