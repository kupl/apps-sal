def elements_sum(arr, d=0):
    summ = 0
    for i in arr:
        try:
            summ += i[len(arr)-(arr.index(i)+1)]
        except IndexError:
            summ += d
    return summ
