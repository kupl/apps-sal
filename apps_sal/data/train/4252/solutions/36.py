def merge_arrays(first, second): 
    # your code here
    mylist=first+second
    return(sorted(list(dict.fromkeys(mylist))))
