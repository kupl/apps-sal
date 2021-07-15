def solve(arr): 
    returnedarray = []
    for item in arr[::-1]:
        if item not in returnedarray:
            returnedarray.insert(0, item)
    return returnedarray
