def solution(m_mass1, m_mass2, g_mass1, g_mass2, vol, temp) :
    return (g_mass1 / m_mass1 + g_mass2 / m_mass2) * 0.082 * (temp + 273.15) / vol
