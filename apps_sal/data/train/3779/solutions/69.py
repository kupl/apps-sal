def past(h, m, s):
    h_to_milli = h * 60 * 60 * 1000
    m_to_milli = m * 60 * 1000
    s_to_milli = s * 1000
    millis = h_to_milli + m_to_milli + s_to_milli
    return millis
