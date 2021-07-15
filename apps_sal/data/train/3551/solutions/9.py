def array_previous_less(arr):
    output = []
    k = 0
    for i in range(0,len(arr)):
        for j in range(i,-1,-1):
            if arr[j] < arr[i]:
                output.append(arr[j])
                k = 1
                break
        if k == 0:
            output.append(-1)
        elif k == 1:
            k = 0
    return output
