def merge_arrays(first, second): 
     first += second
     return list(sorted(set(first),reverse = False))
