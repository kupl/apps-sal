def next_item(my_list, item):
    found = None
    for x in my_list:
        if found:
            return x
        if x == item:
            found = True
    return None
    
# Given a sequence of items and a specific item in that sequence, 
# return the item immediately following the item specified. If the item occurs more than once in a sequence, return the item after the first occurence. 
# This should work for a sequence of any type.  
    
#       Test.assert_equals(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)
#         Test.assert_equals(next_item(['a', 'b', 'c'], 'd'), None)
#         Test.assert_equals(next_item(['a', 'b', 'c'], 'c'), None)

