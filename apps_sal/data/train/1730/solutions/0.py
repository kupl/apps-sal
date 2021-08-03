def two_by_n(n, k):
    vv, vh, hv, hh = k - 1, (k - 1) * (k - 2), k - 2, (k - 1) * (k - 2) + 1
    va, ha, vb, hb = 0, 0, 1, 1
    for i in range(n - 1):
        va, ha, vb, hb = vb, hb, vv * vb + vh * ha, hv * vb + hh * ha
    return (k * vb + k * (k - 1) * ha) % 12345787
