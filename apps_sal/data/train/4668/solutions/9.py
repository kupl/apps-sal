def is_divisible_by_6(s):
    if s == '*':
        return ['0', '6']
    elif s[-1].isdigit() and int(s[-1]) % 2:
        return []
    check = s.index('*')
    res = []
    digit_sum = sum((int(i) for i in s[:check] + s[check + 1:]))
    for i in range(10):
        if check == len(s) - 1 and i % 2 == 0 and ((i + digit_sum) % 3 == 0) or (check != len(s) - 1 and (i + digit_sum) % 3 == 0):
            res.append(str(int(s[:check] + str(i) + s[check + 1:])))
    return res
