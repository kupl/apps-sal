def max_and_min(arr1,arr2):
    l=[]
    for temp1 in arr1:
        for temp2 in arr2:
            l.append(abs(temp1-temp2))
            l.sort()
    return [l[-1],l[0]]
