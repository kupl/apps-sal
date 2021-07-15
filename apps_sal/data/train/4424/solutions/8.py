def expression_matter(a, b, c):
    operations = '+*'
    return max(
        max(eval(f'({a}{op1}{b}){op2}{c}'), eval(f'{a}{op1}({b}{op2}{c})'))
        for op1 in operations
        for op2 in operations
    )
