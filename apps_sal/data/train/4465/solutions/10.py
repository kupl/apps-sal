def super_size(n):
    # your code here
    new = list(str(n))
    new = sorted(new, reverse=True)
    new = ''.join(new)
    return int(new)
