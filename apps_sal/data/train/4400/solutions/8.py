def minimum_steps(num, value):
    num.sort()
    return next((i - 1 for i in range(len(num) + 1) if sum(num[:i]) >= value), 0)
