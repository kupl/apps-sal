import re
from fractions import Fraction as fraction


def solve(*equations):
    A, x, b = parse_equations(equations)
    answer = gaussian_elimination(A, x, b)
    return answer


def parse_equations(equations):
    create_equation = Equation.from_string
    equations = [create_equation(eq) for eq in equations]
    x = []
    for eq in equations:
        for var in eq.variables.keys():
            x.append(var)
    seen = set()
    x = [var for var in x if not (var in seen or seen.add(var))]
    A = []
    b = []
    for i, eq in enumerate(equations):
        A.append([])
        b.append(eq.constant)
        for var in x:
            constant = eq.variables.get(var)
            A[i].append(constant if constant else 0)
    return A, x, b


def gaussian_elimination(A, x, b):
    n = len(A)
    if n < len(x):
        return None  # There will be free variables
    for a, b in zip(A, b):
        a.append(b)
    for i in range(len(x)):
        max_el = abs(A[i][i])
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > max_el:
                max_el = abs(A[j][i])
                max_row = j
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
        a1 = A[i][i]
        if round(a1, 9) == 0:
            return None
        for j in range(i + 1, n):
            a2 = A[j][i]
            if a2 == 0:
                continue
            c = -a2 / a1
            A[j][i] = 0
            for k in range(i + 1, len(x) + 1):
                A[j][k] += c * A[i][k]
    return back_substitution(A, x)


def back_substitution(U, x):
    answer = {}
    col = len(x) - 1
    for row in range(len(U) - 1, -1, -1):
        if U[row][col] == 0:
            if round(U[row][len(x)], 9) != 0:  # b not in C(A)
                return None
            continue
        answer[x[col]] = U[row][len(x)] / U[row][col]
        for i in range(row - 1, -1, -1):
            U[i][len(x)] -= U[i][col] * answer[x[col]]
        col -= 1
    return answer


class Equation:
    def __init__(self, variables, constant):
        self.variables = variables
        self.constant = constant

    @classmethod
    def from_string(cls, eq):
        obj_list = []  # ax+by+cz-5=0 => [a,b,c]
        obj_regex = re.compile(r"-?\d*[a-z]+|-?\d+")

        substring = eq[0: eq.find("=")]
        found_obj = obj_regex.findall(substring)
        if len(found_obj):
            for obj in found_obj:
                obj_list.append(obj)

        substring = eq[eq.find("=") + 1:]
        found_obj = obj_regex.findall(substring)
        if len(found_obj):
            for obj in found_obj:
                obj = obj[1:] if "-" in obj else "-" + obj  # Right hand objects become negative
                obj_list.append(obj)

        s_regex = re.compile(r"[a-z]+")
        constant = -sum(int(obj) for obj in obj_list if not s_regex.search(obj))
        variable_list = [obj for obj in obj_list if s_regex.search(obj)]

        variable_dict = {}
        n_regex = re.compile(r"-?\d*")
        for obj in variable_list:
            s = s_regex.search(obj).group()
            n = n_regex.search(obj).group()
            if n == "-":
                n = -1
            else:
                if n == "":
                    n = 1
                else:
                    n = int(n)
            if variable_dict.get(s):
                variable_dict[s] += n
            else:
                variable_dict[s] = n
        return cls(variable_dict, constant)

    def __repr__(self):
        return "Variables: {}\nConstant: {}".format(self.variables, self.constant)
