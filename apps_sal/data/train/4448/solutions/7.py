def get_derivative(string):
    if string.endswith('x'):
        return string[:-1]
    if 'x^' not in string:
        return '0'
    a, b = string.split('x^')
    return 'x^'.join([str(int(a)*int(b)), str(int(b)-1)]) if b != '2' else str(int(a)*2)+'x'
