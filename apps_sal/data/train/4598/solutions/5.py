import operator
def calculate(n1, n2, o):
    calc = {
        'add':operator.add((int(n1, base=2)),(int(n2, base=2))), 
        'subtract':operator.sub((int(n1, base=2)),(int(n2, base=2))), 
        'multiply':operator.mul((int(n1, base=2)),(int(n2, base=2))) }
    return '{:b}'.format(calc[o])
