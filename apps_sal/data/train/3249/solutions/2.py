def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    n = float(len(x))
    sum_y = sum(y)
    sum_x = sum(x)
    sum_x_squared = sum([x_i * x_i for x_i in x])
    sum_x_y = sum([x_i * y_i for (x_i, y_i) in zip(x, y)])

    divisor = (n * sum_x_squared - (sum_x * sum_x))
    intercept = (sum_x_squared * sum_y - sum_x * sum_x_y) / divisor
    slope = (n * sum_x_y - sum_x * sum_y) / divisor

    return (round(intercept, 4), round(slope, 4))
