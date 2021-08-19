def solve_eq(eq):
    (a1, b1, c1, d1) = eq[0]
    (a2, b2, c2, d2) = eq[1]
    (a3, b3, c3, d3) = eq[2]
    x = (b1 * c2 * d3 - b1 * c3 * d2 - b2 * c1 * d3 + b2 * c3 * d1 + b3 * c1 * d2 - b3 * c2 * d1) / (a1 * b2 * c3 - a1 * b3 * c2 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1)
    y = (-a1 * c2 * d3 + a1 * c3 * d2 + a2 * c1 * d3 - a2 * c3 * d1 - a3 * c1 * d2 + a3 * c2 * d1) / (a1 * b2 * c3 - a1 * b3 * c2 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1)
    z = (a1 * b2 * d3 - a1 * b3 * d2 - a2 * b1 * d3 + a2 * b3 * d1 + a3 * b1 * d2 - a3 * b2 * d1) / (a1 * b2 * c3 - a1 * b3 * c2 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1)
    return [x, y, z]
