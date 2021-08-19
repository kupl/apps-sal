def solve(a, b):
    """
    Used the % operator instead of repeated subtraction of a - 2*b or b - 2*a
    Because as long as a > 2*b, the repeated subtraction has to be done and it will 
    eventually give a % 2*b. Repeated subtration in recursion has the problem of
    exceeding the recursion depth, so this approach is better
    """
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        return solve(a % (2 * b), b)
    elif b >= 2 * a:
        return solve(a, b % (2 * a))
    else:
        return [a, b]
