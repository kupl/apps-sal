def duplicates(arr):
    i=0
    for iter in arr:
        i+=int(arr.count(iter)/2)/arr.count(iter)
    return round(i)
        

