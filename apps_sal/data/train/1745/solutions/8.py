def calculate(exp):
    import re
    s = [float(i) for i in re.findall(r'[.\d]+', exp)]
    ops = exp
    for i in range(10):
        ops = ops.replace(str(i), '')
    ops = ops.replace('.', '')
    p = list(ops)
    for i in ['+', '-', '*', '$']:
        ops = ops.replace(i, '')
    if (ops != '') or (len(p) >= len(s)):
        return '400: Bad request'
    for i in range(len(p)):
        if p[i] == '$':
            o = i
            j = i + 1
            while True:
                if s[j] == 'o':
                    j = j + 1
                else:
                    break
            while True:
                if s[o] == 'o':
                    o = o - 1
                else:
                    break
            s[o] = s[o] / s[j]
            s[j] = 'o'
    for i in range(len(p)):
        if p[i] == '*':
            o = i
            j = i + 1
            while True:
                if s[j] == 'o':
                    j = j + 1
                else:
                    break
            while True:
                if s[o] == 'o':
                    o = o - 1
                else:
                    break
            s[o] = s[o] * s[j]
            s[j] = 'o'
    for i in range(len(p)):
        if p[i] == '-':
            o = i
            j = i + 1
            while True:
                if s[j] == 'o':
                    j = j + 1
                else:
                    break
            while True:
                if s[o] == 'o':
                    o = o - 1
                else:
                    break
            s[o] = s[o] - s[j]
            s[j] = 'o'
    for i in range(len(p)):
        if p[i] == '+':
            o = i
            j = i + 1
            while True:
                if s[j] == 'o':
                    j = j + 1
                else:
                    break
            while True:
                if s[o] == 'o':
                    o = o - 1
                else:
                    break
            s[o] = s[o] + s[j]
            s[j] = 'o'
    for i in s:
        if i != 'o':
            return i
