def capitalize(s):
    return [''.join([(j, j.upper())[i % 2 == 0] for i, j in enumerate(s)]),
            ''.join([(j, j.upper())[i % 2 == 1] for i, j in enumerate(s)])]
