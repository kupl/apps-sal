import copy
import re


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if not (isinstance(self.numerator, int) and isinstance(self.denominator, int)):
            raise ValueError('Expecting integer values.')
        if not self.denominator:
            raise ValueError('Division by 0.')
        self.reduce()

    def reduce(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

    def to_float(self):
        return self.numerator / self.denominator

    @classmethod
    def to_fraction(cls, obj):
        if isinstance(obj, int):
            return Fraction(obj, 1)
        elif isinstance(obj, float):
            i, j = str(obj).split('.')
            return Fraction(int(j) + int(i) * 10 ** len(j), 10 ** len(j))
        else:
            raise ValueError('Only int or float.')

    @staticmethod
    def _gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def _lcm(self, x, y):
        return abs(x * y) // self._gcd(x, y)

    def __add__(self, other):
        lcm = self._lcm(self.denominator, other.denominator)
        numerator = (self.numerator * (lcm // self.denominator)) + (other.numerator * (lcm // other.denominator))
        return Fraction(numerator, lcm)

    def __sub__(self, other):
        lcm = self._lcm(self.denominator, other.denominator)
        numerator = (self.numerator * (lcm // self.denominator)) - (other.numerator * (lcm // other.denominator))
        return Fraction(numerator, lcm)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __bool__(self):
        return self.numerator != 0

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)


class LinearEquation:

    PATTERN = '[+-]?([0-9]+[a-zA-Z]*|[a-zA-Z]+)([+-]([0-9]+[a-zA-Z]*|[a-zA-Z]+))*'

    def __init__(self, eq):
        self.eq = eq.replace(' ', '')
        if not self._validation():
            raise ValueError('Expecting correct Equation.')

    def _validation(self):
        if re.match('^' + LinearEquation.PATTERN + '=' + LinearEquation.PATTERN + '$', self.eq):
            return True
        else:
            return False

    @staticmethod
    def _tokenize(string):
        tokens = re.findall('[+-]?(?:[0-9]+[a-zA-Z]*|[a-zA-Z]+)', string)
        values = dict()
        for token in tokens:
            value, var = re.findall('^([+-]?[0-9]*)([a-zA-Z]*)$', token)[0]
            if not value or value == '+':
                value = Fraction(1, 1)
            elif value == '-':
                value = Fraction(-1, 1)
            else:
                value = Fraction.to_fraction(float(value))
            if var in list(values.keys()):
                values[var] += value
            elif value:
                values[var] = value
        return values

    def parse(self):
        left_side, right_side = self.eq.split('=')
        values = self._tokenize(left_side)
        for var, value in list(self._tokenize(right_side).items()):
            value *= Fraction(-1, 1)
            if var in list(values.keys()):
                values[var] += value
            else:
                values[var] = value
        if '' not in list(values.keys()):
            values[''] = Fraction(0, 1)
        return values


class LinearEquationSystem:

    def __init__(self, m, x, b):
        self.m = m
        self.x = x
        self.b = b
        if not self._validate():
            raise ValueError('Wrong arguments.')

    def _validate(self):
        if not isinstance(self.m, list) and not isinstance(self.x, list) and not isinstance(self.b, list):
            return False
        if not (len(self.m) == len(self.b)):
            return False
        for eq in self.m:
            if not isinstance(eq, list) and len(eq) == len(self.x):
                return False
        return True

    @staticmethod
    def _rank(m):
        rank = min(len(m[0]), len(m))
        ind = min(len(m[0]), len(m))
        for i in range(ind):
            if m[i][i]:
                for j in range(i + 1, len(m)):
                    multiplier = m[j][i] / m[i][i]
                    for k in range(i, len(m[0])):
                        m[j][k] -= (multiplier * m[i][k])
            else:
                reduce = True
                for j in range(i + 1, len(m)):
                    if m[j][i]:
                        reduce = False
                        m[i], m[j] = m[j], m[i]
                        break
                if reduce:
                    rank -= 1
                else:
                    for j in range(i + 1, len(m)):
                        multiplier = m[j][i] / m[i][i]
                        for k in range(i, len(m[0])):
                            m[j][k] -= (multiplier * m[i][k])
        return rank, m

    def solve(self):
        m = copy.deepcopy(self.m)
        m_rank, _ = self._rank(m)
        m_b = copy.deepcopy(self.m)
        for i, row in enumerate(m_b):
            row.append(self.b[i])
        m_b_rank, m_b = self._rank(m_b)

        if m_rank == m_b_rank and m_rank == len(self.x):
            solutions = dict()
            b = list()

            for row in m_b:
                b.append(Fraction(-1, 1) * row[-1])
                del row[-1]
            while len(m_b) > len(m_b[0]):
                del m_b[-1]

            for i in range(len(m_b))[::-1]:
                multiplier = None
                for j in range(len(m_b[i])):
                    if j == i:
                        multiplier = Fraction(1, 1) / m_b[i][i]
                    elif m_b[i][j]:
                        b[i] -= (m_b[i][j] * solutions[self.x[j]])
                solutions[self.x[i]] = b[i] * multiplier

            for var in solutions:
                solutions[var] = solutions[var].to_float()

            return solutions

        else:
            return None

def solve(*eqs):
    print(eqs)
    values_list = list()
    variables = set()
    coefficient_matrix = list()
    b = list()
    for i, eq in enumerate(eqs):
        values_list.append(LinearEquation(eq).parse())
        for var in list(values_list[i].keys()):
            variables.add(var)
        coefficient_matrix.append(list())
    variables = sorted(list(variables))
    for i in range(len(eqs)):
        for var in variables:
            if not var:
                b.append(values_list[i][var])
            elif var in list(values_list[i].keys()):
                coefficient_matrix[i].append(values_list[i][var])
            else:
                coefficient_matrix[i].append(Fraction(0, 1))
    system = LinearEquationSystem(m=coefficient_matrix, x=variables[1::], b=b)
    return system.solve()

