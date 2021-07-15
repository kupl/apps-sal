def find_array(arr1, arr2):
    # Solution
    list1 =[]    
    for num in arr2:
        if num < len(arr1):
            list1.append(arr1[num])
    return list1
