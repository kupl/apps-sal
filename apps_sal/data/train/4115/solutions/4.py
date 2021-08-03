def find_outlier(integers):
    listEven = []
    listOdd = []
    for n in integers:
        if n % 2 == 0:
            listEven.append(n)
        else:
            listOdd.append(n)

    if len(listEven) == 1:
        return listEven[0]
    else:
        return listOdd[0]
