def calculate(s):
    x = [int(i) for i in s.split() if i.isdigit()]
    return sum(x) if 'gains' in s.split() else x[0] - x[1]
