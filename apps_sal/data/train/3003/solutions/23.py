def args_count(*args,**kwargs):
    return len([x for x in args])+len([x for x in kwargs]) 
