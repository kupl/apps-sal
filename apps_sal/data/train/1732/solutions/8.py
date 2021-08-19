def decode_eq_side(eq_side):
    result = {}
    sign, factor, var_name = 1, "", ""

    def add_variable():
        nonlocal factor, var_name, result
        if var_name:
            result[var_name] = result.get(var_name, 0) + sign * int(factor) if factor else result.get(var_name, 0) + sign
        elif factor:
            result[""] = result.get(var_name, 0) + sign * int(factor) if factor else result.get(var_name, 0) + sign
        factor, var_name = "", ""

    for i, s in enumerate(eq_side.replace(" ", "")):
        if s == "+":
            add_variable()
            sign = 1
        elif s == "-":
            add_variable()
            sign = -1
        elif s.isdigit():
            factor += s
        else:
            var_name += s
    else:
        add_variable()
    return result


def decode_equation(equation):
    variables, variables2 = [decode_eq_side(side) for side in equation.split("=")]
    for var, factor in variables2.items():
        variables[var] = variables.get(var, 0) - factor
    variables[""] = -1 * variables.get("", 0)
    return variables


def solve(*equations):
    # get equation variables and matrix
    equations_variables = [decode_equation(equation) for equation in equations]
    variable_names = {var_name for eq_vars in equations_variables for var_name in eq_vars}
    variable_names.discard("")
    variable_names = list(variable_names)
    if len(variable_names) > len(equations_variables):
        return None
    equations_matrix = [[variables.get(var_name, 0) for var_name in variable_names] + [variables.get("", 0)] for variables in equations_variables]
    del equations_variables
    # gauss elimination
    gauss_matrix = []
    for i in range(len(variable_names)):
        chosen_row = max(equations_matrix, key=lambda row: abs(row[i]))
        # check if solution is indeterminate
        if abs(chosen_row[i]) < 1e-10:
            return None
        equations_matrix.remove(chosen_row)
        gauss_matrix.append([0] * i + [param / chosen_row[i] for param in chosen_row[i:]])
        for row_i, row in enumerate(equations_matrix):
            equations_matrix[row_i] = [0] * (i + 1) + [param - row[i] * gauss_matrix[-1][i + j + 1] for j, param in enumerate(row[i + 1:])]
    # check if there are no solution
    if any(abs(row[-1]) > 1e-10 for row in equations_matrix):
        return None
    solution = []
    for equation in reversed(gauss_matrix):
        solution.append(equation[-1] - sum([equation[-(2 + i)] * param for i, param in enumerate(solution)]))
    return dict(zip(variable_names, reversed(solution)))
