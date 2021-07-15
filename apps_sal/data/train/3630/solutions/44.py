def arithmetic(a, b, operator):
    return eval(f'{a}{operator}{b}'.replace('add','+').replace('subtract','-').replace('divide','/').replace('multiply','*'))
