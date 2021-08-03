def men_from_boys(arr):
    dummy = []
    dummy1 = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            dummy.append(i)
        else:
            dummy1.append(i)
    dummy.extend(dummy1[::-1])
    return dummy
