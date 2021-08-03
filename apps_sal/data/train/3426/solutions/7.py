def tax_calculator(t):
    return isinstance(t, (float, int)) and round(max(0, t) * .1 - max(0, t - 10) * .03 - max(0, t - 20) * .02 - max(0, t - 30) * .02, 2)
