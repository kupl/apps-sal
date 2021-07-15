def dont_give_me_five(start,end):
    res = 0
    for n in range(start, end+1):
        if not '5' in str(n):
            res+=1
    return res
