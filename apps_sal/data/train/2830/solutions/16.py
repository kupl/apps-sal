def db_sort(arr): 
     m = sorted(arr, key=lambda x: (isinstance(x, str), x))
     return m
