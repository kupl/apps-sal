import re

def differentiate(equation, point):
    terms = re.findall(r'[-]*[0-9x^]+', equation)
    result = 0
    for term in terms:
        amount = re.search(r'^-*[0-9]+|^-*x', term)
        if amount is not None:
            amount = amount.group(0)
            if amount == 'x':
                amount = 1
            elif amount == "-x":
                amount = -1
            else:
                int(amount)
        power = re.search(r'(?<=\^)\d+$|x+$', term)
        if power is not None:
            power = power.group(0)
            if power.isnumeric():
                result = result + (int(power) * int(amount) * point**(int(power)-1))
            elif power == 'x':
                power = 1
                result = result + (int(amount) * power)
    return result
