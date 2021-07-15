def calculate(n1, n2, o):
    return bin(int(n1, 2) + int(n2, 2) if o == 'add' else int(n1, 2) - int(n2, 2) if o == 'subtract' else int(n1, 2) * int(n2, 2)).replace('0b', '')
