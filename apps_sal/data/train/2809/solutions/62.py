def digitize(n):
    string_num = str(n)
    digits = []
    for digit in string_num:
        digits.append(int(digit))
    digits.reverse()
    return digits
