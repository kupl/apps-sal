def integrate(coef, exp):
    return '{}x^{}'.format(int(coef/(exp+1)) if int(coef/(exp+1)) == coef/(exp+1) else coef/(exp+1), exp+1)
