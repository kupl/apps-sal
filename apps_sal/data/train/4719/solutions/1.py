def sort_array(a):
    odds = []
    evens = []
    newArray = []
    for i in a:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    evens.sort()
    evens.reverse()
    odds.sort()
    for i in range(len(a)):
        if a[i] % 2 == 0:
            newArray.append(evens[0])
            evens.pop(0)
        else:
            newArray.append(odds[0])
            odds.pop(0)
    return newArray
