def balanced_num(number):
    s = str(number)
    part = (len(s) - 1) // 2
    s1 = sum(map(int, s[:part]))
    s2 = sum(map(int, s[-part:]))
    return 'Not ' * (s1 != s2 and len(s) > 2) + 'Balanced'
