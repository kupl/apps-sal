def solution(m1, m2, g1, g2, v, t):
    return (g1 * 0.001 / m1 + g2 * 0.001 / m2) * 0.082 * (t + 273.15) / v * 1000
