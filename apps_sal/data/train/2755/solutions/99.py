def multiple_of_index(arr):
    l = list()
    for i in range(len(arr)):
        print(arr[i],i)
        if i == 0 and arr[i] == 0:
            l.append(i)
        elif i == 0:
            continue
        if arr[i] % i == 0 :
            l.append(arr[i])
    print(l)
    return l
