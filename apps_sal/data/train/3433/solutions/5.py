def replace_zero(arr):
    labels = []
    max = 1
    ans = -1
    # find all the indices that correspond to zero values
    for i in range(len(arr)):
        if arr[i] == 0:
            labels.append(i)
    # try each index and compute the associated length
    for j in range(len(labels)):
        arr[labels[j]] = 1
        count = 1
        end = 0
        # check how long the sequence in on the left side.
        k = labels[j]
        while end == 0 and k != 0:
            if arr[k - 1]:
                count = count + 1
                k = k - 1
            else:
                end = 1
        end = 0
        k = labels[j]
        # check how long the sequence in on the right side.
        while end == 0 and k != len(arr) - 1:
            if arr[k + 1]:
                count = count + 1
                k = k + 1
            else:
                end = 1
        # restore the selected element to zero and check if the new value is a max.
        arr[labels[j]] = 0
        if(count >= max):
            ans = labels[j]
            max = count
    return(ans)
