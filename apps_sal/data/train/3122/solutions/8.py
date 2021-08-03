def chess_triangle(n, m):
    res = 0
    # 3x2 / 2x2
    n_, m_ = n - 1, m - 2
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 8
    n_, m_ = n - 2, m - 1
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 8
    # 4x2 / 2x4
    n_, m_ = n - 1, m - 3
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 8
    n_, m_ = n - 3, m - 1
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 8
    # 4x3 / 3x4
    n_, m_ = n - 2, m - 3
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 8
    n_, m_ = n - 3, m - 2
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 8
    # 3x3
    n_, m_ = n - 2, m - 2
    if 0 < n_ and 0 < m_:
        res += n_ * m_ * 16
    return res
