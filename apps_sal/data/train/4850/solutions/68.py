def solution(mole1, mole2, mass1, mass2, volume, temp) :
    div1 = mass1 / float(mole1)
    div2 = mass2 / float(mole2)
    return (0.082 / float(volume)) * (temp + 273.15) * (div1 + div2)
