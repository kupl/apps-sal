def super_size(n):
    # your code here
    b = sorted([int(x) for x in str(n)], reverse=True)
    return int("".join(map(str, b)))
