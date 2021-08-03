def quadratic(x1, x2):
    x = 1
    formula = (x * x), (x * - (x2)), (-x1 * x), (-x1 * - (x2))
    return formula[0], formula[1] + formula[2], formula[3]
