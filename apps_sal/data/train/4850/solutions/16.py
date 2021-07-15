def solution(mm1, mm2, gm1, gm2, volume, temp) :
    Mass1 = gm1 * 0.001/mm1
    Mass2 = gm2 * 0.001/mm2
    Temperature = temp + 273.15
    answer = (Mass1 + Mass2) * 0.082 * Temperature / volume * 1000
    return answer
