def tokenize(expression):
    result = []
    curr = ''
    for chr in expression:
        if chr.isdigit() or chr == '.':
            curr += chr
        elif chr in '$*-+':
            result.extend([float(curr), chr])
            curr = ''
        else:
            raise ValueError('invalid input')
    if curr:
        result.append(float(curr))
    return result


def calculate(expression):
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '$': lambda x, y: x / y}
    try:
        l = tokenize(expression)
    except ValueError:
        return '400: Bad request'
    for op in '$*-+':
        while op in l:
            i = l.index(op)
            l = l[:i - 1] + [ops[op](l[i - 1], l[i + 1])] + l[i + 2:]
    return l[0]
