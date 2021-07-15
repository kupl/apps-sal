def make_2d_list(head,row,col):
    count = head
    arr2 = []
    for i in range(row):
        arr = []
        for j in range(col):
            arr.append(count)
            count += 1
        arr2.append(arr)
    return arr2
