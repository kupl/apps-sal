def conference_picker(arr1,arr2):
    L=[]
    for i in arr2:
        if i not in arr1:
            return i
            L.append(i)
    if L==[]:
        return 'No worthwhile conferences this year!'
