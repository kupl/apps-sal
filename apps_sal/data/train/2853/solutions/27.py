def solve(arr): 
    newArr = []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] not in newArr: newArr.append(arr[i])
    newArr.reverse()
    return newArr
