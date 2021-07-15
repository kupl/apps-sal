def men_from_boys(arr):
    l1 = sorted(set(arr))
    arr, odds = [], []
    for i in l1:
        if i & 1: odds.append(i)
        else:      arr.append(i)
    l1 = None
    odds.reverse()
    arr.extend(odds)
    return arr #lamda suck, bitwise rock
