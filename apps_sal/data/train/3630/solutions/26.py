def arithmetic(a, b, operator):
    return eval(f'{a}{operator[0].translate(str.maketrans("asmd", "+-*/"))}{b}')
