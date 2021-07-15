def args_count (*args,**kwargs):
    count=0
    for item in args:
        count+=1
    for item in kwargs:
        count+=1
    return(count)    
