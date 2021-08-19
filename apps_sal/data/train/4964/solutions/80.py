def is_uppercase(inp):
    inp = inp.replace(' ', '')
    inp = ''.join(filter(str.isalpha, inp))
    sum1 = sum((1 for c in inp if c.isupper()))
    if sum1 == len(inp):
        return True
    else:
        return False
