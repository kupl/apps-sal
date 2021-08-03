import re

my_regexp = (r'(?P<sign>[+\-]?)'
             r'(?P<coeff>\d*)'
             r'x'
             r'(?:\^(?P<exp>\d+))?')


def as_int(s): return int(s) if s else 1


def derivative(eq):
    result = ''
    for monom in re.finditer(my_regexp, eq):
        sign, coeff, exp = monom.groups()
        coeff, exp = list(map(as_int, (coeff, exp)))
        coeff *= exp
        exp -= 1
        result += ('{sign}{coeff}' if exp == 0 else
                   '{sign}{coeff}x' if exp == 1 else
                   '{sign}{coeff}x^{exp}'
                   ).format(sign=sign, coeff=coeff, exp=exp)
    return result if result else '0'
