def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    for i in arr :
        if not isinstance(i, int) or isinstance(i, bool) : return None
    return sum(i**3 for i in arr if i%2!=0)
