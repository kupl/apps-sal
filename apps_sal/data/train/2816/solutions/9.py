def calculate(s):
    s = s.replace('plus', '+').replace('minus', '-')
    summ = eval(s)
    return str(summ)

