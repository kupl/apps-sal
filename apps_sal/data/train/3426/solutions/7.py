def tax_calculator(t):
    return isinstance(t, (float, int)) and round(max(0, t) * 0.1 - max(0, t - 10) * 0.03 - max(0, t - 20) * 0.02 - max(0, t - 30) * 0.02, 2)
