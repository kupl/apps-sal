def solution(M1,M2,m1,m2,V,T) :
    """ Return Total Pressure P=nRT/V"""
    T += 273.15
    R = 0.082
    n = m1/M1 + m2/M2
    P=(m1/M1 +m2/M2)*R*T/V
    return P
