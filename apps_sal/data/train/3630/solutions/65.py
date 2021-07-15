def arithmetic(a, b, operator):
    kek = {
        "add": '+',
        "subtract": '-',
        "divide": '/',
        "multiply": '*'
    }
    return eval(f'{a} {kek[operator]} {b}')
