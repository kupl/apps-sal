def calculate(a, o, b):
    if a==b==0 and o=='**':return
    try:    return eval(f'{a}{o}{b}')
    except: return
