def super_size(n): 
    return int(''.join(list([str(x) for x in sorted([int(i) for i in str(n)], reverse=True)])))
    

