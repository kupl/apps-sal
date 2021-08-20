def valid_solution(m):

    def is_valid(a):
        return len(a) == 9 and all([i + 1 in a for i in range(9)])

    def get_block_as_row(n):
        return [m[3 * (n / 3) + i / 3][3 * n % 9 + i % 3] for i in range(9)]
    return all([is_valid(r) for r in m]) and all([is_valid([r[i] for r in m]) for i in range(9)]) and all([is_valid(get_block_as_row(i)) for i in range(9)])


validSolution = valid_solution
