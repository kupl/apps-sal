digits = '0123456789'
ops = '+-/*'

def calc(expr):
    r = []
    i = 0
    t = len(expr)
    c = ''
    s = ''
    left = 0
    right = 0
    cur_idx = 0
    while i < t:
        c = expr[i]
        if c in digits:
            if not s:
                s = c
            elif s[-1] in digits:
                s += c
            else:
                r += [s]
                s = c
        elif c == ' ':
            pass
        elif c in ops:
            r += [s] if s != '' else []
            r += [c]
            s = ''
        elif c == '(':
            left = 1
            right = 0
            cur_idx = i
            while i < t and left != right:
                i += 1
                if expr[i] == '(':
                    left += 1
                elif expr[i] == ')':
                    right += 1
            r += [calc(expr[cur_idx+1:i])]
        i += 1
    r += [s] if s != '' else []
    r_new = []
    for item in r:
        try:
            r_new.append(float(item))
        except ValueError:
            r_new.append(item)
    r = list(r_new)
    r_new = []
    i = 0
    t = len(r)
    while i < t:
        if r[i] == '-':
            if type(r[i+1])==float:
                r_new.append(-r[i+1])
            elif r[i+1] == '-':
                sign = 1
                while r[i+1] == '-':
                    sign *= -1
                    i += 1
                r_new.append(sign * r[i])
                i -= 1
            else:
                r_new.append(r[i])
                r_new.append(r[i+1])
            i += 2
        else:
            r_new.append(r[i])
            i += 1
    r_new = [d for d in r_new if d != '']
    while '*' in r_new or '/' in r_new:
        t = len(r_new)
        mul_idx = r_new.index('*') if '*' in r_new else t
        div_idx = r_new.index('/') if '/' in r_new else t
        if mul_idx == 0 or div_idx == 0:
            raise Exception()
        cur_idx = min(mul_idx, div_idx)
        new_numb = r_new[cur_idx-1] * r_new[cur_idx+1] if cur_idx == mul_idx else r_new[cur_idx-1] / r_new[cur_idx+1]
        r_new = r_new[:cur_idx-1] + [new_numb] + r_new[cur_idx+2:]
    return sum([d for d in r_new if d != '+'])
    

def calculate(x):
    if x == '':
        return False
    try:
        return calc(x)
    except:
        return False
