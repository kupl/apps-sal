def merge(array):
    mid = len(array)
    if mid > 1:
        left = merge(array[:(mid//2)])
        right = merge(array[(mid//2):])
        array = []
        
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                array.append(left.pop(0))
            else:
                array.append(right.pop(0))
        if len(left) != 0:
            array.extend(left)
        elif len(right) != 0:
            array.extend(right)
            
    return array
    
def merge_arrays(first, second): 
    return merge(list(set(first + second)))
