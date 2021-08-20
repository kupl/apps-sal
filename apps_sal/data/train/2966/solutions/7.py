def calculate(s):
    return eval(''.join([a for a in s.replace('loses', '-').replace('gains', '+') if a in '0123456789+-']))
