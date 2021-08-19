def calc_type(a, b, c):
    return {a + b: 'addit', a - b: 'subtract', a * b: 'multiplicat', a / b: 'divis'}[c] + 'ion'
