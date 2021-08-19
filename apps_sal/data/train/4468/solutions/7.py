def simplify(number):
    if number == 0:
        return ''
    terms = [f'{c}*{10 ** i}' if i else str(c) for (i, c) in enumerate(str(number)[::-1]) if c > '0']
    return '+'.join(reversed(terms))
