def arithmetic(a, b, operator):
    words_operator = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    return eval('{} {} {}'.format(a, words_operator[operator], b))
