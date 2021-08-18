def replace_zero(arr):
    labels = []
    max = 1
    ans = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            labels.append(i)
    for j in range(len(labels)):
        arr[labels[j]] = 1
        count = 1
        end = 0
        k = labels[j]
        while end == 0 and k != 0:
            if arr[k - 1]:
                count = count + 1
                k = k - 1
            else:
                end = 1
        end = 0
        k = labels[j]
        while end == 0 and k != len(arr) - 1:
            if arr[k + 1]:
                count = count + 1
                k = k + 1
            else:
                end = 1
        arr[labels[j]] = 0
        if(count >= max):
            ans = labels[j]
            max = count
    return(ans)
