def hot_singles(arr1, arr2):
    result = []
    for i in arr1:
        if i not in arr2 and i not in result:
            result.append(i)
    for i in arr2:
        if i not in arr1 and i not in result:
            result.append(i)
            
    return result
    #your code here

