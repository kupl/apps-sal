def digitize(n):
    new_list = list(int(x) for x in str(n))
    return new_list[::-1]
