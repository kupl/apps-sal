def super_size(n):
    digits = [int(i) for i in str(n)]
    new_int = ""
    while digits:
        new_int += str(max(digits))
        digits.remove(max(digits))
    return int(new_int)
