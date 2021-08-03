def heron(a, b, c):
    return round((1 / 4) * (4 * b * b * c * c - (b * b + c * c - a * a)**2)**(1 / 2), 2)
