def multiple_of_index(arr):
    ls=[]
    for i in range(len(arr)):
        if i==0:
            continue
        if arr[i]%i==0:
            ls.append(arr[i])
    return ls
