def dont_give_me_five(start,end):
    return sum([(1,0)['5' in str(x)] for x in range(start,end+1)])
