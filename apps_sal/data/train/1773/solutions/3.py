# PEP 8 - Function names should be in snake_case
def valid_solution(m):
    is_valid = lambda a: len(a) == 9 and all([i + 1 in a for i in range(9)])
    get_block_as_row = lambda n: [m[3 * (n / 3) + (i / 3)][(3 * n) % 9 + i % 3] for i in range(9)]
    return all([is_valid(r) for r in m]) and all([is_valid([r[i] for r in m]) for i in range(9)]) and all([is_valid(get_block_as_row(i)) for i in range(9)])

# Just to pass the Kata
validSolution = valid_solution
