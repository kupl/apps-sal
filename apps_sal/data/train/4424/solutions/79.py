def expression_matter(a, b, c):
    return max(
        max(
            eval('{0} {1} ( {2} {3} {4} )'.format(a, op1, b, op2, c)),
            eval('( {0} {1} {2} ) {3} {4}'.format(a, op1, b, op2, c))
        ) for op1 in '+*' for op2 in '+*'
    )
