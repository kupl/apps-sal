def calculator(x,y,op):
    ops = ['+', '-', '*', '/']
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if x in nums and y in nums and op in ops:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
    else:
        return 'unknown value'
