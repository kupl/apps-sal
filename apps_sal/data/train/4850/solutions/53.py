def solution(mm1, mm2, m1, m2, volume, temp):
    return (m1 / mm1 + m2 / mm2) * 0.082 * (273.15 + temp) / volume
