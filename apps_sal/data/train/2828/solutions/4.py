def power_law(a, b, x):
    return round(a[1] * (b[1] / (a[1] + 1e-09)) ** __import__('math').log(x / (a[0] + 1e-09), b[0] / (a[0] + 1e-09)))
