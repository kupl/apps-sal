def sum_str(a, b):
    return str(int.__add__(*map(lambda s: int(s or '0'), (a, b))))
