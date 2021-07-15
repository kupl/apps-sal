from collections import Counter
def is_zero_balanced(arr):
    if not arr:
        return False
    arr = Counter(arr)
    for element in arr:
        if not arr[element] == arr[-element]:
            return False
    return True    
