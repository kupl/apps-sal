import numpy
def first_non_consecutive(arr):
    if sorted(arr) == list(range(min(arr), max(arr)+1)):
        return None
    else:
        difference = list(numpy.diff(arr))
        for i in difference:
            if i > 1:
                index = difference.index(i)
                return arr[index+1]
        
        
    #your code here

