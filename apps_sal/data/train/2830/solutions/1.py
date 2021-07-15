def db_sort(arr): 
    n=[]
    s=[]
    for i in arr:
        if type(i) ==type( 'a'):
            s.append(i)
        else:
            n.append(i)
    return sorted(n)+sorted(s)
