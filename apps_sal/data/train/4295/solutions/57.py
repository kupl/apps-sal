def balanced_num(number):
    if number <= 99:
        return 'Balanced'
    s = str(number)
    print(number)
    n = int((len(s) - 1) / 2)
    return 'Balanced' if sum((int(c) for c in s[:n])) == sum((int(c) for c in s[-n:])) else 'Not Balanced'
