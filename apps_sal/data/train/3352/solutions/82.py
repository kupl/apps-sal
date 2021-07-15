def find_longest(arr):
    #first we have to check every item of the list
    #variable to store the bigest number
    longest_item = 0
    # we will use it to iterate through the list
    i = 0
    while i < len(arr):
        #if the size of the int stored in the variable is smaller than the tested one, the tested one will replace it.
        if len(str(longest_item)) < len(str(arr[i])):
            longest_item = arr[i]
            i += 1
        #else it will just loop
        else :
            i += 1
    # second we have to return this value
    return longest_item
            
    
    
        
    #your code here

