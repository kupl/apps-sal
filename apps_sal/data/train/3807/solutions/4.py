def smaller(arr):
    a = []
    counter = 0
    for j in range(len(arr)):
        j = arr[0]
        for k in arr:
            if j > k:
                counter += 1
        a.append(counter)
        counter = 0
        arr.remove(arr[0])
    return(a)

