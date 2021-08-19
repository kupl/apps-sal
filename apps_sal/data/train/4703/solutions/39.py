def bar_triang(*dots):
    x_sum = y_sum = 0
    for d in dots:
        x_sum += d[0]
        y_sum += d[1]
    xO = f'{x_sum / 3:.4f}'
    yO = f'{y_sum / 3:.4f}'
    return [float(xO), float(yO)]
