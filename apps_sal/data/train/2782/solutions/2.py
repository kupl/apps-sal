def calc(expr):
    if len(expr.strip()) < 1:
        return 0

    if expr.count('+') == 0 and expr.count('-') == 0 and expr.count('*') == 0 and expr.count('/') == 0:
        return float(expr.split(' ')[-1])

    op_flags = '+-*/'
    nums = []
    ops = []
    expr_list = expr.split(' ')

    for e in expr_list:
        if e in op_flags:
            b = float(nums.pop())
            a = float(nums.pop())

            if e == '+':
                nums.append(a + b)
            elif e == '-':
                nums.append(a - b)
            elif e == "*":
                nums.append(a * b)
            elif e == "/":
                nums.append(a / b)
        else:
            nums.append(e)

    return nums[0]
