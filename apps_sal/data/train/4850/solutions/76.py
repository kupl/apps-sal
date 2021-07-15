def solution(m1, m2, M1, M2, V, T) :
    m1 = M1 * 0.001/m1
    m2 = M2 * 0.001/m2
    T += 273.15
    R = 0.082
    return (m1+m2)*R*T/V*1000
