def calculate(s):
    s = s.replace('minus', ' -')
    s = s.replace('plus', ' ')
    s = s.split(' ')
    s = str(sum([(int(x)) for x in s]))
    return s
