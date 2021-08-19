def generate_number(lst, n):
    lst = set(lst)
    return n if n not in lst else next((9 * d + n for d in range(1, 10) if 0 < n - d < 10 and 9 * d + n not in lst), None)
