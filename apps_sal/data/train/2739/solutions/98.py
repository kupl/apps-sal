def cube_odd(arr):
    arr_cubed =[]
    sum=0
    for element in arr:
    
        if not str(element).isdigit() and not str(element)[0]=='-':
            return None
        else:
            arr_cubed.append(element**3)
    for element in arr_cubed:
        if not element%2==0:
            sum +=element
    return sum
    #your code here - return None if at least a value is not an integer

