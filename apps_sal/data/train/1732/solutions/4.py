import re
from math import gcd

def solve(*eqs):
    # Print equations for reference
    for e in eqs:
        print(e)
    # Parsed equations into values
    parsed_eqs = []
    for e in eqs:
        e = ('' if e[0] == '-' else '+') + e
        parts = re.match(r'\A(([+-][0-9]*[a-z]*)+)=(([+-]?[0-9]*[a-z]*)+)\Z', e).groups()
        parts = parts[0], ('' if parts[2][0] == '-' else '+') + parts[2]
        parts = [re.findall(r'[+-][0-9]*[a-z]*', p) for p in parts]
        parts = [[[''.join(re.findall(r'\A([+-][0-9]*)', i)), ''.join(re.findall(r'[a-z]', i))] for i in p] for p in parts]
        parsed = {}
        for i, p in enumerate(parts):
            for v, k in p:
                if k not in parsed:
                    parsed[k] = 0
                parsed[k] += (int(v) if v not in '-+' else int(v + '1')) * [1, -1][i]
        parsed_eqs.append(parsed)
    # Parsed values into matrix
    keys = set()
    for parsed_eq in parsed_eqs:
        for key in parsed_eq:
            keys.add(key)
    for parsed_eq in parsed_eqs:
        for key in keys:
            if key not in parsed_eq:
                parsed_eq[key] = 0
    ordered_keys = sorted(keys - {''}) + ['']
    print(('\n' + str(ordered_keys)))
    matrix = []
    for parsed_eq in parsed_eqs:
        matrix.append([[parsed_eq[k], 1] for k in ordered_keys])
    for line in matrix:
        print(line)
    # Reduce the matrix with standard operations
    def swap(i0, i1):
        # matrix[i1], matrix[i0] = matrix[i0], matrix[i1]
        tmp = matrix[i0]
        matrix[i0] = matrix[i1]
        matrix[i1] = tmp
    def mul(i, n):
        for l in matrix[i]:
            l[0] *= n
    def div(i, n):
        for l in matrix[i]:
            l[1] *= n
    def add(io, it):
        for c in range(len(matrix[0])):
            matrix[it][c][0] = matrix[it][c][0] * matrix[io][c][1] + matrix[io][c][0] * matrix[it][c][1]
            matrix[it][c][1] *= matrix[io][c][1]
    def sub(io, it):
        for c in range(len(matrix[0])):
            matrix[it][c][0] = matrix[it][c][0] * matrix[io][c][1] - matrix[io][c][0] * matrix[it][c][1]
            matrix[it][c][1] *= matrix[io][c][1]
    def reduce(i):
        for l in matrix[i]:
            divisor = gcd(l[0], l[1])
            if l[1] < 0:
                divisor *= -1
            if divisor != 0:
                l[0], l[1] = l[0] // divisor, l[1] // divisor
    # Convert to row echelon form
    def ref(r0, c0):
        print()
        if r0 >= len(matrix) or c0 >= len(matrix[0])-1:
            return
        if matrix[r0][c0][0] == 0:
            r = r0
            while r < len(matrix) and matrix[r][c0][0] == 0:
                r += 1
            if r == len(matrix):
                return ref(r0, c0+1)
            swap(r0, r)
        for i in range(r0, len(matrix)):
            if matrix[i][c0][0] != 0:
                div(i, matrix[i][c0][0])
                reduce(i)
        for i in range(r0, len(matrix)):
            mul(i, matrix[i][c0][1])
            reduce(i)
        for i in range(r0+1, len(matrix)):
            if matrix[i][c0][0] != 0:
                sub(r0, i)
                reduce(i)
        return ref(r0+1, c0+1)
    ref(0, 0)
    # Remove lines that lack meaning
    matrix = [line for line in matrix 
              if line != [[0, 1] for x in range(len(line))]]
    print('REF:')
    for line in matrix:
        print(line)
    # Generate reduced row echelon form by retracing up the matrix
    def rref(r0, c0):
        while r0 > 0 and c0 > 0 and matrix[r0][c0] != [1, 1]:
            if r0 > 0 and matrix[r0][c0][0] == 0:
                r0 -= 1
            elif c0 > 0 and matrix[r0][c0] != [1, 1]:
                c0 -= 1
        if r0 <= 0 or c0 <= 0:
            return
        for i in range(0, r0):
            matrix[-1] = [[0, 1] for x in range(len(matrix[0]))]
            add(r0, -1)
            div(-1, matrix[i][c0][1])
            mul(-1, matrix[i][c0][0])
            sub(-1, i)
            reduce(i)
        return rref(r0-1, c0-1)
    matrix.append([[0, 1] for x in range(len(matrix[0]))])
    rref(len(matrix)-2, len(matrix[0])-2)
    matrix.pop()
    print()
    for line in matrix:
        print(line)
    print()
    for line in matrix:
        print(line)
    if len(matrix) == 0 or len(matrix) != len(matrix[0]) - 1:
        print(('Bad dimensions: {}, {}'.format(len(matrix), len(matrix[0]))))
        return None
    result = {}
    for i in range(len(matrix)):
        result[ordered_keys[i]] = -matrix[i][-1][0]/matrix[i][-1][1]
    return result

