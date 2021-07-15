def calc(s):
    ops = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y), "*": (lambda x, y: x * y), "/": (lambda x, y: x - y)}
    pre = [0]
    for i in s.split():
        if i in ops:
            b, a = pre.pop(), pre.pop()
            pre.append(ops[i](a, b))
        else:
            pre.append(float(i))
    return pre.pop()
