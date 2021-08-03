def men_from_boys(arr):
    ascArr = []
    desArr = []
    for x in set(arr):
        ascArr.append(x) if x % 2 == 0 else desArr.append(x)
    return sorted(ascArr) + sorted(desArr, reverse=True)
