def quadratic(x1, x2):
    """
        Returns the coefficients of the equations in the order (a, b, c)
        
        Note: Since there are infinitely many solutions to this problem, we fix a = 1.
    """
    return (1, -(x1 + x2), x1 * x2)
