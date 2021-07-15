def minimum(arr):
    #your code here...
    y = 0
    for x in arr :
        if     y == 0 :  y=x
        elif   x < y  :  y=x
    return y
def maximum(arr):
    #...and here
    y = 0
    for x in arr :
        if     y == 0 :  y=x
        elif   x > y  :  y=x
    return y
