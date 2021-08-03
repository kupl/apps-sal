def scf(arr):
    factors_list = []
    dict = {}
    min_list = []
    for element in arr:
        for factor in range(1, element + 1):
            if element % factor == 0:
                factors_list.append(factor)
    for factor in factors_list:
        if factor in dict and factor != 1:
            dict[factor] += 1
        else:
            dict[factor] = 1
    for factor in factors_list:
        if dict[factor] == len(arr):
            min_list.append(factor)
    if min_list != []:
        return min_list[0]
    else:
        return 1
