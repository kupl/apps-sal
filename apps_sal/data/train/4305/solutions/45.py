def order_weight(string):
    string = string.split()
    string = sorted(string)
    string = sorted(string, key=f)
    return ' '.join(string)


def f(n):
    return sum(int(i) for i in n)
