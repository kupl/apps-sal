def filter_homogenous(arrays):
    list = []
    for list1 in arrays:
        n=0
        x=0
        while n<len(list1):
            if type(list1[0])==type(list1[n]):
                n+=1
                x = 1
            else:
                x = -1
                break
        if x == 1:
            list.append(list1)
    return list

