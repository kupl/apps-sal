import re

EQUATION_REGEXP = re.compile(r'^[xy]=(-?\d*)t([+-]\d+)$')


def parse_coefficient(raw_coef):
    if not raw_coef:
        return 1
    elif raw_coef == '-':
        return -1
    return int(raw_coef)


def parse(equation):
    equation = equation.replace(' ', '')
    coefficients = EQUATION_REGEXP.match(equation).groups()
    return list(map(parse_coefficient, coefficients))


def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


def compile_result(mult_a, mult_b, coefs_a, coefs_b):
    multiplier = -1 if mult_a < 0 else 1

    A = mult_a * multiplier
    A = A if A != 1 else ''   
    
    B = abs(mult_b) if abs(mult_b) != 1 else ''
    B_sign = '-' if multiplier * mult_b > 0 else '+'
    
    C = multiplier * (mult_a * coefs_a[1] - mult_b * coefs_b[1])

    return f'{A}x {B_sign} {B}y = {C}'


def para_to_rect(equation_a, equation_b):
    coefs_a = parse(equation_a)
    coefs_b = parse(equation_b)
    parameter_lcm = int(lcm(coefs_a[0], coefs_b[0]))
    mult_a = int(parameter_lcm / coefs_a[0])
    mult_b = int(parameter_lcm / coefs_b[0])
    return compile_result(mult_a, mult_b, coefs_a, coefs_b)
    

