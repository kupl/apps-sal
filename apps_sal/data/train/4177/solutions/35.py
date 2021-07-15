def men_from_boys(arr):
    arr = list(set(arr))
    ascArr = []
    desArr = []
    for x in arr: ascArr.append(x) if x % 2 == 0 else desArr.append(x)
    return sorted(ascArr) + sorted(desArr, reverse=True)

