def something_acci(num_digits):
    a = [1, 1, 2, 2, 3, 3]
    while len(str(a[-1])) < num_digits:
        a.append(a[-1] * a[-2] * a[-3] - a[-4] * a[-5] * a[-6])
    return (len(a), len(str(a[-1])))
