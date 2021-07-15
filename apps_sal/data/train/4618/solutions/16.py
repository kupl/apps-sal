def positive_sum(arr):
    add = 0
    addtemp = 0
    index = 0
    for i in arr:
        if i > 0:
            add = arr[index]
            index += 1
            add = add + addtemp
            addtemp = add
            print(add)
        else:
            print("skipping the {}".format(i))
            index += 1
    if add > 0:
        return(add)
    else:
        return(0)
