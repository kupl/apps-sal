def solve(param):
    a = int('0' + '9' * (len(str(param)) - 1))
    return sum((int(d) for d in str(a) + str(param - a)))
