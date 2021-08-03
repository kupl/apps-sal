def productFib(prod, f1=0, f2=1):
    return [f1, f2, True] if prod == f1 * f2 else [f1, f2, False] if prod < f1 * f2 else productFib(prod, f2, f1 + f2)
