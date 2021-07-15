def sel_reverse(arr,l):
    new_l = []
    index = max(l, 1)
    for x in range(0, len(arr)+1, max(index,l)):
        new_l.extend(arr[x:x+index][::-1])
    return new_l
