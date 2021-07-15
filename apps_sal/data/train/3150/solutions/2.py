def binary_cleaner(seq): 
    return list(filter(lambda x:x<=1, seq )), [ i for i in range(len(seq)) if seq[i]>1 ]
