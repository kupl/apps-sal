def distinct(seq):
    
# =============================================================================
#     This function removes duplicates from an array of numbers and returns it 
#     as a result.
#     The order of the returned sequence is the same as found in the given list
#     
#     Example:
#         distinct([1, 1, 2]) ==> [1, 2]
# =============================================================================
    
    result = []
    
    for num in seq:
        if num not in result:
            result.append(num)
    
    return result
