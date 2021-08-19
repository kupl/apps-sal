def closest_sum(i, ii):
    print(i)
    print(ii)
    iii = len(i)
    iiiiiii = 2.6406429642573826e+32
    for iiii in range(iii):
        for iiiii in range(iii):
            for iiiiii in range(iii):
                if iiii != iiiii and iiiii != iiiiii and (iiiiii != iiii):
                    if abs(i[iiii] + i[iiiii] + i[iiiiii] - ii) < abs(iiiiiii - ii):
                        iiiiiii = i[iiii] + i[iiiii] + i[iiiiii]
    return iiiiiii
