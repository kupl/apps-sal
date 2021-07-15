import sys
def three_amigos(numbers):

    p1 = 0
    min_range = sys.maxsize
    output = None
    
    for idx in range(3, len(numbers)+1):
        slice = numbers[p1:idx]
        p1 += 1
        if sameParity(slice):
            minmax = max(slice) - min(slice)
            if minmax < min_range:
                min_range = minmax
                output = slice
                
    return output if output else []
        
      
    
    
def sameParity(arr):
    even = True if arr[0] % 2 == 0 else False
    
    for idx in range(1, len(arr)):
        if even and arr[idx] % 2 != 0:
            return False
        if not even and arr[idx] % 2 == 0:
            return False
            
    return True
