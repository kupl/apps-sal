
def args_count(*arg,**kwarg):
    count = 0
    for i in kwarg:
        count+=1
    for j in arg:
        count+=1

    return count
