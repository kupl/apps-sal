def sum_from_string(s):
    return sum(map(int, "".join(c if c.isdigit() else " " for c in s).split()))
