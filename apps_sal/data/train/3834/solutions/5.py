def palin(a, b):
    n = (a - 1) // 2
    x, y = divmod(b - 1, 10 ** n)
    result = str(x + 1) + (a > 2) * f'{y:0{n}}'
    return int(result + result[-1 + (a%-2)::-1])
