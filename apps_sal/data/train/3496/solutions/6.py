def sort_by_area(arr): 
    return sorted(arr, key=lambda x: (x[0]*x[1] if isinstance(x,tuple) else x*x*3.14))
