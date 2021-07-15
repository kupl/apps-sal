def max_and_min(arr1,arr2):
    max_min = [abs(y-x) for x in arr1 for y in arr2]
                        
    return [max(max_min), min(max_min)]
