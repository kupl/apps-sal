def calc_type(a, b, res):
    dict = {a + b: 'addition', a - b: 'subtraction', a * b: 'multiplication', a / b: 'division'}
    return dict[res]
