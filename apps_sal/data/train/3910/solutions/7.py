def operator_insertor(n):
    min = 9
    for a1 in ['+', '-', '']:
        for a2 in ['+', '-', '']:
            for a3 in ['+', '-', '']:
                for a4 in ['+', '-', '']:
                    for a5 in ['+', '-', '']:
                        for a6 in ['+', '-', '']:
                            for a7 in ['+', '-', '']:
                                for a8 in ['+', '-', '']:
                                    expression = "1{}2{}3{}4{}5{}6{}7{}8{}9".format(a1, a2, a3, a4, a5, a6, a7, a8)
                                    signs = len(expression) - 9
                                    if (eval(expression) == n) and (min > signs):
                                        min = signs
    if min == 9:
        return None
    else:
        return min
