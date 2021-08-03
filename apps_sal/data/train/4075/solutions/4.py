def something_acci(num_digits):
    x = [1, 1, 2, 2, 3, 3]
    while True:
        if len(str(x[-1])) >= num_digits:
            return (len(x), len(str(x[-1])))
        else:
            x.append(x[-1] * x[-2] * x[-3] - x[-4] * x[-5] * x[-6])
