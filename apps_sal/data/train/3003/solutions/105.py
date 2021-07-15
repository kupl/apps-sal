def args_count(*params,**params2):
    result=0
    for i in params:
        result+=1
    for i in params2:
        result+=1
    return result
