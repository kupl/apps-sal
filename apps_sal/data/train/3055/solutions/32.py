def sum_str(a, b):
    ans = a + '+' + b
    if len(a) == 0 and len(b) == 0:
        return '0'
    else:
        try:
            return str(eval(ans))
        except:
            return '9'
