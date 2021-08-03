def balanced_num(number):
    s = str(number)
    if len(s) % 2 == 0:
        a, b = s[:len(s) // 2 - 1], s[len(s) // 2 + 1:]
    else:
        a, b = s[:len(s) // 2], s[len(s) // 2 + 1:]
    return 'Balanced' if sum(int(d) for d in a) == sum(int(d) for d in b) else 'Not Balanced'
