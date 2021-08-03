from itertools import zip_longest

ADDER = {
    ('0', '0', '0'): ('0', '0'),
    ('0', '0', '1'): ('1', '0'),
    ('0', '1', '0'): ('1', '0'),
    ('0', '1', '1'): ('0', '1'),
    ('1', '0', '0'): ('1', '0'),
    ('1', '0', '1'): ('0', '1'),
    ('1', '1', '0'): ('0', '1'),
    ('1', '1', '1'): ('1', '1'),
}


def add(x, y):
    x = x.lstrip('0')
    y = y.lstrip('0')

    if not x:
        return y or '0'
    elif not y:
        return x

    sum_digits, carry = [], '0'
    for x_digit, y_digit in zip_longest(x[::-1], y[::-1], fillvalue='0'):
        sum_digit, carry = ADDER[(x_digit, y_digit, carry)]
        sum_digits.append(sum_digit)

    if carry == '1':
        sum_digits.append(carry)

    return ''.join(sum_digits)[::-1]
