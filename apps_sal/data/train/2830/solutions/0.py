def db_sort(arr): 
    return sorted(arr, key=lambda x: (isinstance(x,str),x))
